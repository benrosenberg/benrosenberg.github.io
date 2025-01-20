
# Programming languages cont.

Classification of programming languages:

compiled languages                                 | interpreted languages
---------------------------------------------------|-----------------------------------------------------
C, C++, Rust, Assembly                             | Java, Python, JavaScript, C#
**advantages**                                     | **advantages**
speed (of execution, not compilation)              | convenience - portability/not linked to architecture
some programs require executables (close-to-metal) | **disadvantages**
**disadvantages**                                  | slow due to overhead of interpreter
platform-dependent/not portable                    |

# CPU cores

To make CPUs faster, initial method was to increase frequency. But after we reached the physical limits of frequency, turned to CPU cores - add "more CPUs"

A single CPU has multiple cores

**A *CPU core* is an independent instruction execution unit within the CPU**

Think of CPU as having little sub-CPUs - those are its cores

Each core has its own registers, instruction pipeline, etc.

Terminology - dual-core, quad-core, octa-core...

In our course by default, we discuss single-core CPUs

## (end of "reminder" section, now we begin the performance section)

# Performance

Things that impact performance:

- Hardware efficiency
  - CPU clock - impacts frequency. As the frequency with which the clock sends synchronization signals increases, the performance of the machine increases
    - But frequency is not everything - used to be, but is not the only important thing anymore
  - Also important - CPU architecture. Good CPU design decisions make the CPU faster
  - Number of CPU cores - more cores is typically better (but a given program will only benefit from multi-core processing if it is written to take advantage of them)
  - Cache - speeds up average CPU-RAM interactions, making performance better
  - RAM - can be a bottleneck, so want fast RAM
  - Hard disk - also can be a bottleneck
    - Speed of hard disk defines how fast programs *start* execution
    - First step of program execution is to copy from hard disk to RAM
- Software efficiency
  - Program efficiency - more important than hardware!
  - Compiler efficiency - also important but performance differences between compilers are minimal compared to program efficiency improvements