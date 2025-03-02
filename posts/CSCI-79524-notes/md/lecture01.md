# Lecture 1

prof's first time teaching course, will fill out syllabus later (topics, etc. - due to 260, 340 not being prereqs)

because of this, some material from 340 and 260 will be discussed towards beginning of course

prof may be late to class b/c previous class is far away

course book - no official textbook. original idea was to take course from prev. prof but will be major differences. may provide links for addt'l material for the course

will try to cover material in course but may assign self-study material

will assign one extra assignment to masters students (official requirement)

current grading idea - 3 assignments (4 for masters students), midterm and final exams

will try to make 340 material part interactive b/c 50% of class has taken 340 already

no attendance grade except same check as 260

grading percentages will be decided on eventually

similar rules to 260 w.r.t. homework requirements

slack - contact via stack channel, link will be in syllabus, same as 260

office hours are joint with 340 students, on days where there are classes (same as 260) - days & times tbd

language will be c++, but will be doing mpi stuff as well

---

first, discuss parallel computing (high-level)

then, discuss 340 material - processes, threads, synchronization

then continue to actual parallel computing material

parallel computing rationale:

- want fast computers
  - computation-intensive applications:
    - games, graphics, llms/ml, gene sequencing/medical research, simulations

methods:

- cpu speed limit reached a while ago - power wall
- memory limit is even worse
- modern approach: add more cores to cpus, etc.
  - instead of faster, do things simultaneously
  - same approach in memory with dual channel memory, and in individual cpu cores with pipelining
  - concept of "SuperScalar" cpu:
    - batch fetching: fetch multiple instructions, have multiple pipelines with multiple issue stations, multiple ALUs, analyze instructions and reorder for better performance (out-of-order execution), etc.
    - (not covered in our course - not something actionable to us, just built-in to cpu)
- vector instructions, SIMD (won't deal with in this course)
  - special vector registers that can store multiple values in cpu, special vector instructions that can process these registers at the same time
- next idea:
  - first, there were multiple CPUs in a computer (supercomputers)
    - however, expensive - individual caches, etc.
  - next, cpu cores - individual/(almost) independent execution unit within cpu
    - kind of like jamming multiple cpus into a single cpu
    - but can do better
  - next, clusters - multiple computers working on same task simultaneously
    - e.g., beowulf - free software to create compute clusters
  - graphics - computationally intense, very parallelism-friendly
    - GPU - cpu optimized for graphical tasks
    - cpu with many weak cores
      - modern cpu may have 64 cores, modern gpu may have 10s of 1000s of cores
    - gpus can be used for non-graphical tasks as well:
      - CUDA - library for nvidia gpus
      - examples: crypto mining, llm training

however, can only take advantage of multiple cores if program is optimized for it/written with multiple cores in mind; by default just running on single core

note - only can expect a speedup proportional to core amount for parts of program that are parallelism-friendly

- example: difference between bringing stack of bricks from one place to another (parallelism-friendly), and baking a cake (not parallelism-friendly)

as a rule: if half of program can be parallelized, and other half cannot, will take at least half the unparallelized time regardless of the amount of compute thrown at it

classic parallel computing course would have discussed e.g. scientific computations. these people will typically use libraries/packages that use these techniques

but we will also discuss concurrency - have multiple cores doing different things simultaneously

- example: when asked to read file from hard disk, program is put to sleep - the call to read the file is "blocking"
  - usually program is more complicated, however - e.g. for a text editor, still need to run user interface
  - can do these things simulataneously

concurrency is very related to parallel programming - do work on same task in parallel case; in concurrent case, different tasks/different work







