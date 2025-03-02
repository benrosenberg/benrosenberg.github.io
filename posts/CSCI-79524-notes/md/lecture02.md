# Lecture 2


office hours start next week - north building, 520F 3:15-5:15

---

some devices have powerful and weak cores - weak cores used when device is idle to save power

some tasks are parallelism-friendy, some are not

example:

- filling array with powers of two
  - should fill in ascending order, but in theory can fill in any order, so could be parallelism-friendly
- filling array with fibonacci numbers
  - typically need to use previous results for next results, so not as friendly (for now assume you don't use formula for n-th fibonacci number)

amdahl's law:

- tries to describe on a theoretical level the benefit we get from adding cores/workers
- suppose we have a task such that fraction $x$ of the task can be done in parallel
- the whole task completes in $N$ seconds on one core/cpu
- then, on $\alpha$ cores, the execution time will be $Nx+ N(1-x)/\alpha$
- speedup will then be $N$ divided by the above, so $\frac{1}{1-x+\frac{x}{\alpha}}$

example: suppose $N=100$ and $x=0.8$, then we have the following variation when we introduce new cores:

| core count | time   |
|------------|--------|
| 1          | 100    |
| 2          | 60     |
| 3          | 46.667 |
| 4          | 40     |
| 5          | 36     |

the time will never reach 20 seconds, regardless of how much compute we throw at it

takeaway: adding cores has diminishing returns

**data dependency graph**: 

- can create a DAG (directed acyclic graph) that represents the prerequisite relationships between data processing tasks
  - example: recipe for a classic soviet salad (!)
    - need to boil eggs, carrots, potatoes before they can each be cut, but the tasks of cutting the boiled items are not dependent on each other. then, need to mix ingredients only once all the ingredients have been cut

**process**: 

- program *in execution*
- involves more than just program code - memory allocated, i/o device access, open files, grabbed locks, etc.
- process is program code in conjunction with all resources allocated to the running program
- we could take the same program and run it twice at the same time, but there will be two independent processes
- if we have two different computers connected via network, we can split the problem in two parts, and send the parts to each of the computers
- having multiple processes doing the same thing enables parallel programming
- if we have multiple cores or threads, though, it may be possible to run in parallel with the same process

**process lifetime**:

- when we know what process expects from the computer, we know how to run it efficiently
- process state/life cycle:
  - first: "i want to run a program"
    - process must be created to run program/application
    - while process is only created, we say it is in the "new" state
    - OS will create a record of the process, called the "process control block" (PCB)
      - in OS's internal bookkeeping, the OS creates a record of the process creation
      - includes process ID, list of files opened for it, memory usage information (e.g. page table), etc.
    - as soon as this PCB appears, the process appears
    - but not yet ready to be executed - program code has not been copied over to memory yet
  - next: process creation is finished
    - first, process wants to use the CPU, in order to run program code
    - however, there are other processes running on the computer at the same time - chance that cpu is idle is not 100%; may be many processes competing for the cpu/waiting to use the cpu
      - list of processes ready and waiting to use cpu right now: **ready queue**
    - processes in ready queue are said to be in the "ready state"
  - next: process is in ready-queue, OS is deciding which process to have running on the CPU
    - could e.g. be using a priority-based queue scheduling algorithm; next chosen process may not be first one in queue
    - when process is chosen by OS to begin running on CPU, and is running on the CPU, it is in the "running state"
  - now process is running on cpu
    - performing machine cycles - fetch, decode, execute, write back
    - ok, until cpu runs into instruction to read or write data to/from file (hard disk) - very slow
    - as soon as process requests any i/o operation (file reading, reading document from hard disk, etc.), the cpu **yields** the cpu to another process while expensive operation takes place
    - assume the action is reading from hard disk - the hard disk has its own queue, so the process gets into another line - **i/o queue**
      - every i/o device has its own queue
      - (as with cpu's ready-queue, not really a true queue, could depend on priority or OS's scheduling algorithm)
    - while process is in i/o queue, or being served by hard disk - while it does not need to use the cpu - it is in the "waiting" state
  - then, data is received from hard disk and needs cpu again
    - process goes back into the waiting state
  - another possible path - OS removes process from CPU and puts back into ready-queue
    - called "pre-emption"
    - can occur if process uses cpu for too long, etc.
      - another possible cause for OS removing proces from CPU - process obtaining a lock, or an interrupt - actions that take a lot of time and don't require CPU
    - depends on cpu scheduling algorithm
  - at some point, process reaches the end
    - process is "deleted" and goes into the terminated state
    - for various reasons, the OS doesn't immediately truly delete the process
- note: while these things are happening, the process is still in the same location in memory
  - doesn't actually move. state changes are effected by updates to PCB (process control block) record


process states:

1. new - process exists, but is not yet ready to be truly executed
2. ready - process is in ready queue, waiting for cpu access
3. running - process is running on the CPU
4. waiting - process is doing something else and does not need the CPU (e.g. using hard disk)
5. terminated - process is done running

- note: questions to ask after lecture
  - how can OS interrupt currently running process on CPU?
    - ask this next lecture so he can go over it
    - basic idea - in e.g. case where process is time-limited, OS tells cpu clock when to issue special "interrupt" instruction, which will return control to CPU
