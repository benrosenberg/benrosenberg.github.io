# Lecture 8


(continuing with multithreading program from last time - finding max of large array)

```cpp
#include <thread>
#include <iostream>
#include <vector>
#include <limits>
#include <chrono>
#include <algorithm>

constexpr int VECTOR_SIZE = 10'000'000;
constexpr int NUM_THREADS = 4;

void FindMax(const std::vector<int>& nums, int from, int upto, int& result) {
    int best = std::numeric_limits<int>::min();
    for (int i = from; i < upto; i++) {
        if (nums[i] > best) {
            best = nums[i];
        }
    }
    result = best;
}

void main() {
    std::vector<int> nums(VECTOR_SIZE);

    // pretend this is unsorted
    for (int i = 0; i < VECTOR_SIZE; i++)
        nums[i] = i + 1;

    // linear scan
    std::chrono::steady_clock::time_point start, finish;

    int result = 0;
    start = std::chrono::steady_clock::now();
    FindMax(nums, 0, VECTOR_SIZE, result);
    finish = std::chrono::steady_clock::now();
    
    std::cout << result << std::endl;

    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(
        finish - start
    ).count() << std::endl;

    std::vector<std::thread> threads;

    int threadPortion = VECTOR_SIZE / NUM_THREADS;
    std::vector<int> results(NUM_THREADS, 0);

    start = std::chrono::steady_clock::now();
    for (int i = 0; i < NUM_THREADS; i++) {
        // there is a problem here - fourth parameter
        // is integer reference variable - results[i]
        // thread library does not automatically convert
        // variables to references, because it is bug-prone
        // so, we need to explicitly treat the variable
        // as a reference ourselves
        threads.emplace_back(
            FindMax, nums, threadPortion * i,
            threadPortion * (i + 1), std::ref(results[i])
        );
    }

    // need to wait for other threads to finish their work
    for (int i = 0; i < NUM_THREADS; i++) {
        // block until threads[i] is finished
        threads[i].join();
    }

    // if we just do this immediately, threads may not be done yet,
    // so we had to wait above using join function
    result = *std::max_element(results.begin(), results.end());
    finish = std::chrono::steady_clock::now();

    std::cout << result << std::endl;

    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(
        finish - start
    ).count() << std::endl;

    return 0;
}
```

reminder - threads can be moved, but not copied. 

- thread objects represent a single thread
- so, copying would mean creating a new thread - doesn't make sense, should just create thread explicitly
- moving means stealing the thread from the previous object

notes on above program:

- using wall time, not cpu time, so may be inaccurate
- there are other tools for measuring performance/runtime - visual studio has some build in (not exam material) - but in general can be complicated
- takeaway: measuring time is hard. usually will just measure elapsed time (wall clock time), but keep in mind that it can't fully represent cpu time and performance of program - may use alternative tools instead

on our computers, this program is actually slower with multithreading:

- reason is that thread creation is expensive
- note: should remember trick where we create breakpoint at thread creation and measure time to create a thread
  - will be useful when measuring difference between multithreaded and singlethreaded solution
  - on project - may be asked to measure amount of time to create a thread on the computer
- amdahl's law does not take this additional time to create threads into account

other thing that may affect program performance: debug vs. release build

- debug builds are much slower because many checks are introduced to assist with debugging - larger program and much slower
- release build is for when development is finished - build for speed and efficiency - fast and small
- profiling should be done in release build, not debug build
  - no sense introducing multiple threads unless you ask your compiler to do things fast

note - for home project, don't just reproduce code from class 1:1 - but can use as a reference

consideration: what if we replace the `best` variable definition with just directly modifying `result`?

```cpp
// create `best` var
int best = std::numeric_limits<int>::min();
// use `result` inplace
result = std::numeric_limits<int>::min();
```

- this ends up being slower
- reason: worse cache efficiency
  - ram slower than cpu registers due to reading & writing - latency (e.g., memory stall)
  - ram is also slow in the sense of throughput - memory bus can be filled
    - in a regular sequential program, this throughput issue is not typically encountered
    - example - nvidia gpu - each streaming multiprocessor can do around 7k operations with 32-bit floating point numbers per clock cycle
    - so, each can do around 39 trillion float point ops per second - 39 terabytes per second
    - however, we only have way less bandwidth - around 2000gbs or 2 terabytes. channel bandwidth is not even remotely sufficient
    - for most operations, are limited by memory throughput
- caches make the latency problem less critical
