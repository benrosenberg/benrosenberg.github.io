# Lecture 3

review - last time, discussed the following about processes:

- process is a program in execution - memory used, other resources, etc.
- pcb (process control block), record of process information (metadata) kept by OS - includes process ID (pid), etc.
- process life cycle - new, ready, running, waiting, terminated
- process sits in ready and i/o queues depending on whether it's waiting for cpu or for i/o device

---

MPI: message passing interface

example: process creation for efficiency

- have MPI cluster of computers, and are using MPI tools 
- install MPI on 6 different computers, connected together on some kind of network
- then, take one program, and ask MPI to launch the program in 6 different processes
  - MPI will take the program code, and create 6 different processes - 6 different executions of the code
  - ideally, each computer should run its own copy (for max utilization/efficiency)
- may be more efficient to create more than 6 processes (even if we assume single-core CPU computers), because then when a process is waiting for disk access/hard disk, the other process could use the cpu, so that the different components of the computer are utilized - spinning their wheels for less time
  - something that is not taken into account by amdahl's law

note on MPI: 

- not a tool, but rather a specification
- there are various implementations of this spec, including OpenMPI, which we will use

---

## threads

processes are "heavy" - lots of information associated with program code - turn to threads

threads:

- each process has a program counter, which tells the cpu the next instruction to execute
- if we introduce another cpu core, we can introduce another program counter for that core
  - we can have the program counter point to the same memory area (not necessarily the same address) as the first one
  - points to the same program code
- these independent executions of the same program code, in the same process, from different program counters, are called **threads**
- each process starts with one single thread of execution

*side note*: context switching: 

- switching from having cpu doing one thing to another thing is not free - has some overhead
- switching from one process to another process takes longer than switching from one thread to another of the same process

difference between process and thread:

- each process:
  - has the same program code
  - may have different data passed in
  - different location in memory - exist independently
  - advantage: don't need to run on the same computer, as in a computational cluster
  - advantage: for concurrent computing (different tasks), need processes because they can use different program code
  - advantage: fault-independent
    - if we deal with threads belonging to the same process, one thread could cause an issue that corrupts/crashes the entire process (all threads crash) - OS will kill process
    - but for processes, if one crashes the rest can continue
- each thread:
  - same program code
  - same data passed in
  - same location in memory
  - advantage: more memory-efficient
  - advantage: threads are "faster"
    - instructions are executed at the same speed, but context switching has less overhead between threads than between processes
  - advantage: threads are faster to create and delete
    - no need to allocate new chunk of memory and copy memory
    - for processes, can fork - copy process - much faster than creating new process, but still expensive to use memory when compared to cpu
  - advantage: built-in, automatic shared memory - allows threads to talk to each other by default

to create a new thread on the same process:

- create small "thread control block" - record describing one additional thread
- not free, but very fast compared to process

in general: threads are lighter, easier, and cheaper, but not always possible


shared vs. not shared in threads in the same process:

- threads belonging to the same process share:
  - program code (text section)
  - data section (where static & global variables are stored)
  - heap section (where dynamically allocated data is stored in memory)
- threads belonging to the same process does not share:
  - stack (function call frames, function data/variables)

example:

```c++
int glob = 123;

int foo(int var) {
    float value;

    // using global variable (shared)
    // available to both t1 and t2
    // all threads access the same var
    // can cause race conditions
    cout << glob++;
}

int main() {
    // need to do #include <thread>
    // or something similar
    std::thread t1(foo, 3);
    std::thread t2(foo, 24);
    // now, this process has 3 threads -
    // original thread plus two newly created

    // the original thread proceeds and prints "Hi"
    cout << "Hi";

    // then, threads t1 and t2 begin running foo
    // with different parameters, indepedently
    // the threads can have different parameters
    // because they do not share the stack
}
```