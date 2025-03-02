# Lecture 5


last time - showed example of how same code could produce different results when run different times. result is no longer deterministic

```c++
#include<iostream>
#include<thread>

void Greet(std::string name) {
    std::cout << "Hello from " << name << std::endl;
}

int main() {
    std::thread t1{ Greet, "t1" };
    std::thread t2{ Greet, "t2" };
    std::cout << "Hello from original" << std::endl;
}
```

this caused error when we ran:

- when original process finishes, whole program finishes
- OS complains that other threads were not terminated manually - t1 and t2 are still trying to run, so "abnormal termination"

to make computer happy, do it in the correct way:

- create thread, and pause & wait for thread to finish

```c++
#include<iostream>
#include<thread>

void Greet(std::string name) {
    std::cout << "Hello from " << name << std::endl;
}

int main() {
    std::thread t1{ Greet, "t1" };
    std::thread t2{ Greet, "t2" };
    std::cout << "Hello from original" << std::endl;

    // join: stop here, and wait for thread to terminate
    // (if thread is done already, no pauses are introduced)
    t1.join();
    t2.join();
}
```

the `join` method is the first example of synchronization: we are controlling the order of the thread termination

the above code does not cause any error messages, because we are terminating the threads explicitly, so no chance that threads are still running when main thread finishes

typical example of race condition:

```c++
#include<iostream>
#include<thread>

int glob{ 0 };

void Foo(std::string name) {
    for (int i{0}; i < 100'000; i++)
        glob++;
}

int main() {
    std::thread t1{ Foo };
    std::thread t2{ Foo };

    t1.join();
    t2.join();

    // less than 200k due to race condition
    std::cout << glob << std::endl;
}
```

global variable is shared between multiple threads, because it is in the data section

issue in above code: multiple threads accessing and modifying same variable

**race condition**: "data race" between two or more threads

- have `glob` variable, initialized to 0
- thread 1 and thread 2 both try to do `glob++`
  - for the sake of discussion, these threads run in parallel on two different cores
- since we don't know which core/which thread will do `glob++` first, we don't know what order instructions will be executed in
- in reality, `glob++` instruction is as follows (mips assembly):

```mips
# assume addr in t0
lw $s0, 0($t0)
addi $s0, $s0, 1
sw $s0, 0($t0)
```

- same thing will happen in both threads, so one thread could read a stale value, and then overwrite the saved value, effectively skipping an increment
- for example: registers for each thread receive 0 as the first value from the load word instruction, then add 1, and then each writes back - regardless of which is first, the value in `glob` is still 1 and not 2
- same/similar scenario when multitasking on same core - context switch could occur before last instruction runs on one of the threads, which would cause the same issue
  - in this case, context switch is likely because of memory access
- could also not run into an issue - possible that tasks happen to run in series (execution does not overlap), in which case `glob` would have 2
- to avoid data corruption, want to access shared data only one process/thread at a time. shared resources should only be accessed by one entity at a time
- name for pieces/fragments of code that should not overlap in execution: **critical sections**. need to prevent execution of critical sections from overlapping

so, definition of **race condition**: bad scenario where we corrupt shared resource/data because of simultaneous access by multiple threads or processes, when at least one tries to modify a shared resource

(however, if only read-only access, then not an issue - only an issue when modification occurs)

"nastiest kind of errors" because they are not reliably reproducible

if only one thread modifying and other reading, can still cause issues:

- may need several operations to modify value (e.g., updating first and second halves of the integer separately)
- will cause data fetched by reading thread to be corrupted
- only an issue if multiple operations are needed to modify the value as needed
- but should avoid in general - e.g., different hardware could have different results
- compiler may actually help with this - c++ has "atomic" class that helps to avoid race conditions
  - compiler can tell whether hardware permits "atomic" modifications

simple way to avoid race condition: "locks"

- have global shared data/device/file
- associate one extra shared variable: "lock"
- "mutex" lock - mutual exclusion
  - simple integer, or boolean variable
- two states: "acquired" or "released", or in cpp, "locked" and "unlocked"
- all processes that deal with shared resource need to be aware that there is a shared lock associated with this resource
- all threads need to be acquire/lock the resource before using it

example: mutex locking:

```c++
#include<iostream>
#include<thread>
#include<mutex>

int glob{ 0 };
std::mutex m;

void Foo(std::string name) {
    for (int i{0}; i < 100'000; i++) {
        // acquire the mutex m
        // scenario 1: if lock is free, close it
        //  and proceed further
        // scenario 2: if lock is not free,
        //  freeze and do not proceed further until
        //  lock is released (and when it is released,
        //  lock again)
        m.lock();
        // critical section of code
        glob++;
        // once finished, open the lock to allow others
        // to use the variable
        m.unlock();
    }
}

int main() {
    std::thread t1{ Foo };
    std::thread t2{ Foo };

    t1.join();
    t2.join();

    // should be 200k due to avoiding race condition
    std::cout << glob << std::endl;
}
```

above is not an efficient solution, but is a solution nonetheless

the above negates the benefit of threads because all work is done in series and not parallel