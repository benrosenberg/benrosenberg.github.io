# Lecture 4

clarification - interrupts:

- first thing happens on hardware level
- interrupt arrives via a wire - cpu is wired to stop all current activities, and jump to a specific location in memory where the OS keeps the interrupt handling functions

clarification - context switching:

- only an issue if the same cpu core running two different processes vs. threads - if two different cores, context switching isn't an issue because the cores are independent execution units

example of reason to create threads even if only one core: webserver

- main loop to listen and serve requests, constantly running
- multiple threads allow for serving users in parallel ("simultaneously")
- every time request is created, create extra thread, and launch serving function in separate thread
- if we have more threads than cores, then some cores start multi-tasking between threads
  - some overhead for switching between threads, even on same core
  - but still better than blocking until first user is done

**multitasking**: quickly switching core from one task to another

- typically not possible to truly run two threads on one core, but can "fake" it by switching back and forth - creates illusion of simultaneous progress on all threads if done fast enough
- hardware may be built with multiple threads in mind - each core is capable of running multiple threads "simultaneously"
  - e.g., a computer with 4 cores may have more than 4 (e.g., 8) "logical processors" - multithreading technology built into cpu, so each core is ready to deal with 2 separate "logical processors"
  - CPUs may be super scalar - ready to execute several instructions simultaneously, e.g. it is ok to run `add $s0, $s1, $s2` and `add $t0, $t1, $t2` at the same time
  - CPUs may permit out-of-order execution - run instructions in order that allows for parallelization
  - CPUs may have vector instruction and special vector registers - single instruction, multiple data
  - for CPUs to run multiple threads, would need a separate program counter for each thread, and need second set of registers - multiple register files
  - fancy features come at a price though - complexity means more complex control circuitry: more hardware, so takes up more space
- other benefit to multitasking - avoid memory stalls (cpu waiting to load data from ram). cpu can execute instructions from the second thread while the first one is stalled

different kinds of threads: kernel threads and user threads

- kernel thread: thread created with help from operating system, typically uses syscall
- user thread: thread created and managed in userspace without involving OS, typically does not require syscall
  - some minor performance benefits
  - but have limitations - OS does not know about thread
  - in userspace, threads can be combined together to multitask on cpu - faster because do not need to alert operating system
    - running is not faster because cpu speed is the same, but creating/switching etc. is faster because OS does not need to be alerted
  - limitation - OS does not know about thread, so if one thread does something blocking (e.g. file reading), OS will freeze both threads (not just the first one) because of how long file reading takes, if the OS does not know about it
  - also not super convenient - kernel threads are typically used now for convenience rather than user threads

thread project example:

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

sample output:

```plaintext
Hello from original
Hello from t2
Hello from t1
```

output does not necessarily come in same order:

- threads work simultaneously
- not possible to know or guarantee which thread prints first
  - even if on same core, cpu scheduling algorithm may be nondeterministic
- can make bugs very hard to detect and fix

another possible output:

```plaintext
Hello from original
Hello from Hello from t1
t2
```

above, `cout` is shared between threads - caused a **race condition**

next time - will discuss interprocess communication and synchronization
