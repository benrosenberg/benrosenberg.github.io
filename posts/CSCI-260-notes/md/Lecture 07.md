
Another example problem:

> Question: Computer A runs at 250 picoseconds (ps) per cycle and has CPI 2 cycles/instruction, and computer B runs at 500 ps/cycle and has CPI of 1.2 cycles/instruction. Which is faster and by how much?
>
> Answer:
> Seconds per instruction of A = 2 cycles/instruction * 250 ps/cycle = 500 ps/instruction
> Seconds per instruction of B = 1.2 cycles/instruction * 500 ps/cycle = 600 ps/instruction
> Therefore, A is 600/500 = 1.2 times faster than B

Yet another example problem:

> Question: Compiler designer is deciding between two code sequences when compiling to a specific PC architecture. He is given this information:

type of instruction|A|B|C
-|-|-|-
CPI|1|2|3

code sequence|A|B|C|
-|-|-|-|-
1|2|1|2|number of inst. for code seq 1
2|4|1|1|number of inst. for code seq 2

> How many total instructions for each code sequence? What is the total number of cycles for each code sequence? What is the CPI for each code sequence?
>
> Answer:
> Total instructions code seq 1 = 2 instructions + 1 instruction + 2 instructions = 5 instructions
> Total instructions code seq 2 = 4 instructions + 1 instruction + 1 instruction = 6 instructions
> Total cycles for code seq 1 = 2 instructions * 1 cycle/instruction + 1 instruction * 2 cycles/instruction + 2 instructions * 3 cycles/instruction = 2 instr. + 2 instr. + 6 instr. = 10 instructions
> Total cycles for code seq 2 = 4 instructions * 1 cycle/instr + 1 instruction * 2 cycles/instr + 1 instruction * 3 cycles/instr = 9 instructions
> CPI of code seq 1 = 10 cycles / 5 instructions = 2 cycles/instruction
> CPI of code seq 2 = 9 cycles / 6 instructions = 1.5 cycles/instruction

Yet *another* example:

> Question: Given the same table above for cycles per each instruction type A, B, C, we are also given the following information about the composition of a program into instruction types:

|A|B|C
-|-|-|-
proportion|50%|35%|15%

> What is the total CPI of this program?
>
> Answer:
> Total CPI = 0.5 * 1 cycle/instruction + 0.35 * 2 cycles/instruction + 0.15 * 3 cycles/instruction = 0.5 cycles/instruction + 0.7 cycles/instr + 0.45 cycles/instr = 1.65 cycles/instr

# Power wall

This section is about the power wall. 

**The *power wall* describes the physical limitations that prevent us from making faster computers.**

When we increase frequency, more heat is generated so the CPU overheats.

This is an issue because electrical components can get overheated - the transistors in the CPU will begin to misbehave when heat is increased.

**A *transistor* is a small element with an incoming wire, outgoing wire, and one other "switch" wire that determines whether current flows through the incoming and outcoing wire.**

There is no sufficiently efficient way to cool CPUs, so we cannot increase frequency.
