# Lecture 6

last time - discussed how threads accessing the same memory location can cause race conditions ("data race")

processes can have similar issues, with shared memory - block of memory allocated by OS for processes to share. incorrect use of this shared memory can cause race conditions

processes and threads can also both have race conditions with shared resources like i/o devices

last time, also discussed technique for mitigating race conditions - lock/mutex

analogy for mutex lock: bathroom lock. enter bathroom and lock, perform task, unlock and next thread can access.

how does the special object of the mutex class work?

- comparison: global bool variable `unlocked = true`

```cpp
// example of bad code
// busy loop until lock opens
while (!unlocked) {}
// "acquire" lock
// however, won't work as desired because
// two threads could read unlocked to be True
// at the same time, and simultaneously modify
// `glob`
unlocked = false;
glob++;
unlocked = true;
```

- issue: how can we prevent race conditions for the lock itself?
- answer: `lock` and `unlock` operation of `mutex` class are **thread-safe**
  - in other words, it is "secured from race conditions"
  - even if two threads are operating simultaneously and arrive at the `m.lock()` instruction at the same time, something lower-level will prevent race conditions for `m`
- how is it possible for `m` to be thread-safe?
  - hardware has this problem in mind: CPU knows special set of instructions called **atomic instructions**
  - atomic instructions are meant to few actions as if they were a single action
    - e.g., for above example, the `!unlocked` check takes several instructions - load, check, and return value. 
    - atomic instructions would do all these actions in a single instruction, to prevent race conditions
  - additional constraint on atomic instructions: only able to execute one time at once on the entire computer
    - implemented via a queue - if two threads try to simultaneously perform an atomic operation, only one will do it and the other will freeze and wait for the previous thread to end

example atomic function: `test_and_set(&lock)`:

- takes pointer to lock var
- if value is true, sets it to false, and returns original value of lock
- few actions completed as one action
- in this course, we will not deal with atomic functions - use more convenient tools - but these convenient tools are enabled by the existence of atomic functions

thread-safe terminology is not just for mutexes and synchronization tools, but also for regular functions

- example: instead of using `std::vec` vector, could use custom container that is thread-safe for e.g. the function `push_back()`
- would mean that we can use `push_back()` without doing anything special - will work with multiple threads without issue
- (if `push_back` were not thread-safe, then could cause race condition - may overwrite last element of vector if two threads try to push_back on that vector at the same time)

question: why not make everything thread-safe?

- answer: efficiency/performance
- locking/unlocking is not cheap - atomic operations are nontrivial
  - e.g. for atomic operations - lock entire address bus, etc.
  - usually has significant performance overhead
  - thread safety is nice, but comes at a price
- another drawback: unpredictability
  - guaranteeing execution times becomes much harder when locking/unlocking things

(note: `unlock` doesn't need to be thread-safe, just `lock`)

our previous example with `m.lock()` is not efficient:

- "heavy contention" for lock
- threads are fighting for control
- want to minimize number of times that we grab and receive locks
- in our example, would be better to lock before and after loop (see below)

```c++
...

int glob{ 0 };
std::mutex m;

void Foo(std::string name) {
    m.lock()
    for (int i{0}; i < 100'000; i++) {
        glob++;
    }
    m.unlock()
}

...
```

reminder: always need to remember to unlock a shared resource

RAII: "resource allocation is initialization"

- when you dynamically acquire a resource, make releasing it automatic
- in case of memory - dynamically allocating memory - do something like garbage collection (e.g., smart pointers)
- in case of mutexes - use something like `lock_guard` - very similar to smart pointer
  - no need to unlock manually
  - once lock guard goes out of scope, releases lock automatically (similar to smart pointers which release memory automatically when they go out of scope)

example with `lock_guard`:

```c++
...

int glob{ 0 };
std::mutex m;

void Foo(std::string name) {
    std::lock_guard<std::mutex> m_guard{ m };
    for (int i{0}; i < 100'000; i++) {
        glob++;
    }
    // no need to unlock - only locked in function scope
}

...
```

currently, `mutex` is our synchronization tool - allows us to avoid race conditions by making sure a shared resouce is used by only one entity/thread/process at a time

however, there are other tools as well:

- conditional variables
- semaphores
- atomic classes
- etc.

many different options because scenarios may require different approaches

for the purposes of our course, we will just stick with mutexes, unless we need more tools

## deadlock

sample piece of code:

```cpp
// each variable has mutex associated with it
int g1, g2;
std::mutex m1, m2;

void t1_func() {
    m1.lock();
    m2.lock();
    ...
    m1.unlock();
    m2.unlock();
}

void t2_func() {
    m2.lock();
    m1.lock();
    ...
    m2.unlock();
    m1.lock();
}
```

the above threads are individually well-written, will not cause race conditions, but have another hazard: deadlock:

- t1 and t2 may arrive at code in parallel
- t1 locks m1, and t2 locks m2
- neither thread can progress because the next required lock is already possessed by the other thread
- this cyclical dependency is known as **deadlock**, another synchronization problem
- deadlock: problematic situation where multiple threads or processes wait for each other, and none can progress
- not guaranteed to happen (like race condition) - detecting is expensive computationally, many OSes do not even try to detect them