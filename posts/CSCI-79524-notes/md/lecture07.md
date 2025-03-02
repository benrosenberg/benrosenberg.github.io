# Lecture 7


reminder: deadlock: two or more processes waiting for resources in a cyclic dependency structure, such that none can progress

two main parallelism hazards so far:

- data race/race condition
- deadlock

sample parallelized program:

- have unsorted array of integers
- want to find largest element in the array
- idea: split array into sections, and use the threads to scan each section simultaneously
- then, do a linear scan of the local maxima and return the max

```cpp
#include <thread>
#include <iostream>
#include <vector>
#include <limits>
#include <chrono>

// typically don't like global vars b/c they are a common
// source of bugs, but this an exception - constexpr means
// it is both constant and allows for significant optimizations
constexpr int VECTOR_SIZE = 10'000'000;

constexpr int NUM_THREADS = 4;

void FindMax(const std::vector<int>& nums, int from, int upto, int& result) {
    // standard cpp threads will discard
    // the return of the upper level function
    // as a result, will need a different way to return
    // cpp recommends two ways - either exceptions,
    // or shared vars. we will use shared vars

    // both input and result are taken by reference
    // vector is constant reference - will not modify
    // but will modify result, so not const
    // passed by reference for efficiency - do not need to copy
    // passing by value would require copying entire vec
    // so each thread would take as much time as a linear scan
    // would defeat the purpose of parallelizatio
    
    // verbose, but this is the modern c++ way to determine
    // the minimum value on the system
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

    // try running simple linear scan for comparison
    std::chrono::steady_clock::time_point start, finish;

    int result = 0;
    start = std::chrono::steady_clock::now();
    FindMax(nums, 0, VECTOR_SIZE, result);
    finish = std::chrono::steady_clock::now();
    
    std::cout << result << std::endl;

    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(
        finish - start
    ).count() << std::endl;

    // run with NUM_THREADS threads
    std::vector<std::thread> threads;
    
    // assume it just works without having a remainder
    int threadPartition = VECTOR_SIZE / NUM_THREADS;
    // allocate space for results
    std::vector<int> results(NUM_THREADS, 0);

    // note: does NOT work, because attempting to reference
    // a deleted function
    // deleted function: copy constructor
    // different constructors - move/copy constructors
    // copy constructor creates new object as a copy of
    // an existing one
    // issue: using copy constructor here will cause
    // copied object to reference same thread
    // therefore, thread object cannot be copy-constructed
    // issue is because push_back is by value, not reference
    // thread class is an example of a class that does not
    // allow any copies - no copy constructors or copy assignment
    // similar concept for smart pointers/unique ptr
    /*
    for (int i = 0; i < NUM_THREADS; i++) {
        std::thread temp{
            FindMax, threadPortion * i,
            threadPortion * (i + 1), results[i]
        };
        threads.push_back(temp);
    }
    */

    // better way
    /*
    for (int i = 0; i < NUM_THREADS; i++) {
        threads.push_back(std::thread{
            FindMax, threadPortion * i,threadPortion * (i + 1), results[i] 
        });
    }
    */

    // best way
    for (int i = 0; i < NUM_THREADS; i++) {
        // start constructing object inside vector by
        // passing parameters directly
        threads.emplace_back(
            FindMax, threadPortion * i,
            threadPortion * (i + 1), results[i]
        );
    }
}
```

note: still issues with the above code, will resolve next lecture
