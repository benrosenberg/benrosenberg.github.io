# Made with help from Google Gemini 2.5 Flash, 2025-09-27

# --- WORD LISTS ---
# T: The true word bank (the target word MUST be in this list).
# G: The valid guess set (a superset of T). For simplicity in this small program,
# we use the same list for both, but the logic allows G to be larger than T.
# Using a larger G (e.g., all 5-letter English words) would be more accurate
# to the prompt but requires a much larger dictionary file.

# with open("valid_words.txt", "r") as f:
#     WORD_LIST = [w.strip() for w in f.readlines()]

with open("word_bank.txt", "r") as f:
    WORD_BANK = [w.strip().upper() for w in f.readlines()]

import functools
import multiprocessing
import os


# --- LEVENSHTEIN DISTANCE IMPLEMENTATION (CACHED) ---
# Caching is essential for performance as it avoids re-calculating the same
# distance pair (A, B) across all guess calculations within a single process.
@functools.lru_cache(maxsize=None)
def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculates the Levenshtein (edit) distance between two strings using memoization.
    We enforce an order to maximize cache hits, as L(s1, s2) = L(s2, s1).
    """
    # Enforce consistent argument order for optimal caching (cache symmetry)
    if s1 > s2:
        s1, s2 = s2, s1

    if s1 == s2:
        return 0

    # Optimized dynamic programming approach (using only one row)
    distances = list(range(len(s2) + 1))

    for i in range(1, len(s1) + 1):
        prev_diag = distances[0]
        distances[0] = i

        for j in range(1, len(s2) + 1):
            temp = distances[j]
            cost = 0 if s1[i - 1] == s2[j - 1] else 1

            distances[j] = min(distances[j] + 1, distances[j - 1] + 1, prev_diag + cost)
            prev_diag = temp

    return distances[len(s2)]


# --- HELPER FUNCTION FOR PARALLEL PROCESSING ---
def _calculate_guess_score(
    guess_and_candidates: tuple[str, list[str]],
) -> tuple[int, str, bool]:
    """
    Calculates the worst-case score for a single guess word against all candidates.
    Designed to be run by the multiprocessing pool.
    This calls the cached levenshtein_distance.
    """
    guess, candidates = guess_and_candidates

    # Map: distance -> count of candidates resulting in that distance
    partition_sizes = {}

    # Determine the size of the partitions this guess would create
    for candidate in candidates:
        # Calls the cached distance function
        distance = levenshtein_distance(guess, candidate)
        partition_sizes[distance] = partition_sizes.get(distance, 0) + 1

    # The worst case is the size of the largest partition (the most words left)
    worst_case = max(partition_sizes.values()) if partition_sizes else 0

    # Return (worst_case, guess, is_candidate)
    return worst_case, guess, (guess in candidates)


# --- STRATEGY CORE FUNCTIONS ---


def find_best_guess(candidates: list[str], guess_set: list[str]) -> tuple[str, int]:
    """
    Implements the Minimax strategy, using multiprocessing for speed.
    """

    if not candidates:
        return "ERROR", 0
    if len(candidates) == 1:
        return candidates[0], 1

    best_guess = None
    min_worst_case = float("inf")

    print(f"  Calculating optimal guess among {len(guess_set)} words...")
    potential_guesses = guess_set

    # ----------------------------------------------------
    # PHASE 1: Parallel Calculation for Large Candidate Sets
    # ----------------------------------------------------

    # Prepare data for parallel processing: [(guess, candidates), (guess, candidates), ...]
    pool_data = [(guess, candidates) for guess in potential_guesses]

    # Determine the number of CPU cores to use
    num_cpus = os.cpu_count() or 4
    print(f"  Using {num_cpus} cores for parallel computation...")

    # Use Pool.map to distribute the workload
    with multiprocessing.Pool(processes=num_cpus) as pool:
        # results is a list of tuples: (worst_case, guess, is_candidate)
        results = pool.map(_calculate_guess_score, pool_data)

    # ----------------------------------------------------
    # PHASE 2: Minimax Selection from Results
    # ----------------------------------------------------

    for worst_case, guess, is_candidate in results:

        # Optimization: If we find a guess that reduces the remaining words to 1, take it.
        if worst_case == 1 and len(candidates) > 1:
            min_worst_case = worst_case
            best_guess = guess
            break

        # Minimax: Find the guess that minimizes the size of the worst-case partition
        if worst_case < min_worst_case:
            min_worst_case = worst_case
            best_guess = guess

        # Tie-breaker: If worst cases are equal, prefer a word that is itself a candidate
        elif (
            worst_case == min_worst_case
            and is_candidate
            and (best_guess is None or best_guess not in candidates)
        ):
            best_guess = guess

    return best_guess, min_worst_case


def main():
    """Runs the interactive Wordle solver."""

    # Multiprocessing safety check (required for Windows and macOS)
    if not __name__ == "__main__":
        print("Error: The script must be run directly to enable multiprocessing.")
        return

    # --- INITIALIZATION ---
    candidates = WORD_BANK[:]
    guess_set = WORD_BANK[:]
    guesses_made = 0

    print("--- Edit Distance Wordle Solver ---")
    print(f"Target word is 5 letters, chosen from a bank of {len(WORD_BANK)} words.")
    print("Strategy: Hardcoded first guess, then Minimax with parallel computation.")
    print("-----------------------------------")

    try:
        while len(candidates) > 1:
            guesses_made += 1
            print(f"\n--- Guess {guesses_made} ---")
            print(f"Current Candidates Remaining: {len(candidates)}")

            best_guess = None
            min_worst_case = float("inf")

            # --- INITIAL GUESS LOGIC: SAUTE or MINIMAX ---
            if guesses_made == 1:
                best_guess = "SAUTE"
                print("  Using hardcoded starting guess: SAUTE")

                # --- NEW DIAGNOSTIC: Calculate and print the full distribution for SAUTE ---
                print(
                    "  Running initial diagnostic check (brief calculation required)..."
                )
                # Since this is a one-off calculation, we run it on the main process
                temp_worst_case, _, _ = _calculate_guess_score((best_guess, candidates))

                # Get the full partition map
                partition_sizes = {}
                for candidate in candidates:
                    distance = levenshtein_distance(best_guess, candidate)
                    partition_sizes[distance] = partition_sizes.get(distance, 0) + 1

                print("  --------------------------------------------------")
                print(
                    f"  SAUTE Distance Distribution (Total: {len(candidates)} words):"
                )
                sorted_distances = sorted(partition_sizes.keys())
                for dist in range(6):  # Check distances 0 through 5
                    count = partition_sizes.get(dist, 0)
                    print(f"    Distance {dist}: {count} words")
                print(f"  Worst Case Partition Size: {temp_worst_case}")
                min_worst_case = (
                    temp_worst_case  # Use the actual worst case for the printout below
                )
                print("  --------------------------------------------------")

            else:
                # 1. Find the mathematically optimal guess using parallel computation
                best_guess, min_worst_case = find_best_guess(candidates, guess_set)

            # Print remaining candidates only if the list is very small
            if len(candidates) < 10:
                print(f"Remaining candidates: {candidates}")

            if len(candidates) == 2:
                # If only two are left, guessing one of them is the 1-bit information guess
                print(f"Only 2 candidates remain. Guessing one of them...")
                best_guess = candidates[0]

            if best_guess:
                print(
                    f"Optimal Guess: {best_guess}"
                    + (
                        f" (Worst case remaining: {min_worst_case} words)"
                        if min_worst_case != float("inf")
                        else ""
                    )
                )

            # 2. Get user input (the crucial feedback)
            user_distance = -1
            while True:
                try:
                    user_distance = int(
                        input(f"Enter the Levenshtein distance for '{best_guess}': ")
                    )
                    if (
                        0 <= user_distance <= 5
                    ):  # Max possible distance for 5-letter words
                        break
                    else:
                        print("Distance must be between 0 and 5.")
                except ValueError:
                    print("Invalid input. Please enter an integer distance.")

            # 3. Check for immediate win
            if user_distance == 0:
                print(
                    f"\n✅ SUCCESS! The word was '{best_guess}'. Found in {guesses_made} guesses."
                )
                cache_info = levenshtein_distance.cache_info()
                print(
                    f"Cache Hits: {cache_info.hits}, Cache Misses: {cache_info.misses}"
                )
                return

            # 4. Filter the candidates based on the provided distance
            new_candidates = []
            print(f"  Filtering {len(candidates)} candidates...")

            # --- DIAGNOSTIC PRINT: Show calculated distances against remaining candidates ---
            if len(candidates) > 1 and len(candidates) < 5:
                print(
                    f"  Diagnostics for last guess '{best_guess}' (Expected distance: {user_distance}):"
                )
                for candidate in candidates:
                    calculated_distance = levenshtein_distance(best_guess, candidate)
                    print(f"    - '{candidate}' distance is {calculated_distance}")
                print("  --------------------------------------------------")
            # ----------------------------------------------------------------------------

            for candidate in candidates:
                # Calculate the distance between the guess and the candidate (CACHED CALL)
                calculated_distance = levenshtein_distance(best_guess, candidate)

                # If the calculated distance matches the user-provided distance,
                # this word is still a possible solution.
                if calculated_distance == user_distance:
                    new_candidates.append(candidate)

            if not new_candidates:
                # This is the error point: contradiction found.
                print(
                    "\n\n❌ ERROR: The provided distance contradicts all remaining candidates."
                )
                print(
                    "Please re-run the script. Pay close attention to the Diagnostic printout above (if visible)."
                )
                print(
                    "The error is highly likely due to a previous incorrect distance input or a mismatched word bank."
                )
                return

            candidates = new_candidates

            # 5. Check remaining candidates after filtering
            if len(candidates) == 1:
                print(f"\n--- Guess {guesses_made + 1} ---")
                print(f"Only one word remains: '{candidates[0]}'.")
                print(f"Input this word now to win!")

                user_final_distance = int(
                    input(f"Enter the Levenshtein distance for '{candidates[0]}': ")
                )
                if user_final_distance == 0:
                    print(
                        f"\n✅ SUCCESS! The word was '{candidates[0]}'. Found in {guesses_made + 1} guesses."
                    )
                else:
                    print(
                        f"\n❌ ERROR: The provided distance ({user_final_distance}) for the last word is not 0."
                    )
                    print(
                        "The solver concluded the word must be this, but your distance feedback was incorrect."
                    )

                cache_info = levenshtein_distance.cache_info()
                print(
                    f"Cache Hits: {cache_info.hits}, Cache Misses: {cache_info.misses}"
                )
                return

    except KeyboardInterrupt:
        print("\n\nSolver interrupted. Goodbye!")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
