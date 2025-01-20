# Syllabus

Items of note:

- Use Slack link ASAP, as it expires within 30 days
- Midterm date is unknown - based on the speed with which we cover the material
- Final date is known already based on the CUNY schedule, but may change (although unlikely)
- No homework resubmissions

Class is split into 4 parts:

1. Review of material from previous classes
2. Performance, and some performance-related calculations
3. Assembly language - MIPS
4. CPU design

Lists of topics for each part will be published throughout the semester. These lists will be useful for reviewing content for the midterm and final exams.

# Review of prior course material

How do computers work?

- Computers just store numbers and do simple arithemtic
- Data is meaningful non-program information
- CPU executes instructions in order
- **The *CPU* is a hardware component responsible for executing instructions**

Note: definitions will be asked on exams. Be specific, or points will be deducted.

- **A *machine cycle* is the sequence of steps a CPU goes through to execute a single instruction**
- Note that a machine cycle is *not* the same as a clock cycle, especially in modern CPUs

Machine cycle steps:

1. Fetch - fetch an instruction from memory, and bring it into the CPU
2. Decode - prepare for instruction execution
3. Execute - execute the instruction
4. Write-back - if result must be placed somewhere, do it in this step

RAM and the CPU:

- Instructions come from the RAM to the CPU
- Data also comes from RAM
- During fetch step, instructions are copied to CPU registers

Registers:

- There are two types of registers:
  - General-purpose CPU registers, and
  - Special-purpose CPU registers
- General purpose registers - to be used by programs. We will use these registers when writing our MIPS programs
- Special purpose registers - registers with special purpose in the CPU, e.g. the instruction register which has the instruction to be executed next

*Side note: registers are also present in I/O devices, used to control them*

RAM vs. CPU speed:

- All running programs must be in RAM - only place CPU can fetch instructions or data from
- Hard disk data and programs must be loaded into RAM first, before CPU can access them
- Speed in this context is the time it takes to read/write data.
- CPU registers are basically instant for our purposes
- RAM is "slow" (compared to CPU)
- For example, addition in the CPU could take around 20 cycles, while reading from RAM could take around 400 cycles
- CPU instructions include loading from and storing to RAM

*Side note: we are already at or near the physical limit for RAM speed. Also, VRAM and RAM are similar in speed, the only caveat is that it takes longer to move things between RAM and VRAM*

- Because RAM is slow, we try to minimize reads and writes to/from RAM
- RAM speed is a big bottleneck for CPU/computer speed
- **A *memory stall* occurs when the CPU has to wait for RAM to deliver necessary data**
- A memory stall is an inefficiency that can sometimes be optimized away by a compiler by reordering instructions.
  - Compilers try to minimize memory stalls, but are not always successful
- Memory stalls still happen all the time
- Individual memory stalls are not on their own perceptible as the CPU is still fast, but in aggregate they can be noticeable

RAM:

- **We say something is *random access* if it takes roughly the same amount of time to access a piece of data, no matter where it is physically on the device**
- Not all memory is random access
- Some non-RAM devices can be random access too