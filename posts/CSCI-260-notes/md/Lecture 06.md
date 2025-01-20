
Benchmarking - run the same program on different computers to compare them.

**A *benchmark* is a standard program used to compare the performance of computers.**

Typically run as a suite, to test all different components of a computer.

Note: performance-related problems will appear on midterm/final.

We said that frequency was the number of signals sent by a CPU clock every second. 

Frequency is measured in Hertz (abbr. Hz) which is the inverse of a second. 5 Hz means 5 times per second or one time per 0.2 seconds.

## SI prefixes

prefix | full prefix | meaning    | value | full value
-------|-------------|------------|-------|------------------
G      | Giga        | 1 billion  | 1e9   | 1,000,000,000
M      | Mega        | 1 million  | 1e6   | 1,000,000
k      | kilo        | 1 thousand | 1e3   | 1,000
T      | Tera        | 1 trillion | 1e12  | 1,000,000,000,000

For example 2,500,000,000 Hz = 2.5 GHz, and 0.5 GHz = 500 MHz = 500,000 kHz = 500,000,000 Hz

### Byte prefixes

Bytes are different. Memory is usually measured in powers of 2:

byte amount | more accurate amount | amount
-|-|-
kB|kiB|2^10
MB|MiB|2^20
GB|GiB|2^30
TB|TiB|2^40

In the real world, always assume that the SI prefix (k,M,etc.) corresponds to the "i" prefix (powers of 2) when working with bytes, even if it is not supposed to by definition.

## Execution time

Execution time is how long a program runs.

There is a difference between elapsed time and CPU time. The CPU may pause to work on something else. In this course when we say execution time, we mean CPU time, not elapsed time.

Say there are two programs, P1 which takes 10 seconds and P2 which takes 15 seconds. We say P1 is 1.5 times faster than P2. 

Note that we did not say 5 seconds faster. In this class, we always compare using ratios or percentages, not flat amounts.

(Dynamic) instruction count - the number of instructions run by the CPU.

When we talk about instruction count, we mean dynamic instruction count. Not every instruction will be run by the CPU due to conditionals, and some may be run a lot due to loops.

Dynamic instruction count is the number of instructions the CPU executes in order to finish the program.

***CPI* - cycles per instruction.**

Some instructions take more clock cycles or ticks to execute than others.

When we say cycles, we refer to CPU clock cycles.

These cycles are *not* the same as machine cycles.

The Average CPI is the total number of cycles divided by the dynamic instruction count.

For example, 1 million instructions, 2.1 cycles per instruction means 2.1 million cycles.

Note: use **units** in calculations to receive credit.

The unit for CPI is cycles/instruction.

(Using units is helpful because they can assist in validating answers.)

Note that average CPI can in reality be below 1 because modern CPUs execute some instructions in parallel.

Example problem:

> Question: Program runs on CPU A in 10s and A is 2 GHz. Want CPU B to run it in 6s. B has 1.2 times as many clock cycles as program A. What CPU frequency should we target for B?
>
> Answer: 
> Total cycles for A = 2,000,000,000 cycles/second * 10 seconds = 20e9 cycles.
> Total cycles for B = 1.2 * total cycles of A = 1.2 * 20e9 cycles = 24e9 cycles
> Clock rate of B = 24e9 cycles/6 seconds = 4e9 cycles/second = 4 GHz
