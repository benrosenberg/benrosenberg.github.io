

Power wall - we don't care about formulas or anything, just care about ideas

***Overclock* - raise frequency above recommended level, can be dangerous**

Can lower the amount of heat generated in the CPU by reducing the amount of electricity through the CPU:

- Generating less heat means we can raise frequency
- We also use less power
- And we have longer battery life

But we can't use too little electricity. If the voltage drops too low, we won't be able to distinguish between on and off states in transistors. Transistor leakage will mean that "off" transistors could be seen as "on".

***Transistor leakage* - phenomena of electricity leaking through the transistor in the "off" state**

# Assembly language programming

Assembly language - 

- IS a programming language
- is NOT machine language
- IS specific to CPU architecture

Assembly language, at a high level:

- All other programming languages are meant to be convenient for programmers - they have complicated abstractions used for application development.
- But the idea of assembly language is to closely represent CPU instructions.
- We use assembly to get complete control over what the CPU is doing.
- Even in C or C++, there isn't a way to interact directly with the CPU - the compiler still sits in the middle.
- ASM instructions are basically English versions of the CPU instructions
- Typical use case - make function very efficient. Outperforming compilers is difficult but can maybe be done for short programs
- More common use case - read generated ASM to see what is going on under the hood. Compiler can provide ASM output for debugging purposes
- ASM is a COMPILED language. No reason to have an interpreter - meant to deal directly with the CPU
- ASM is specific to CPU architecture - meant to represent CPU instructions, so will differ by CPU type

***CPU architecture* - set of rules/specifications to create a CPU of a certain type**

***Instruction Set Architecture (ISA)***:

- **set of available CPU instructions**
- **Number of CPU registers** (e.g. for MIPS, 32 general purpose CPU registers)
- **Word size/register size** (e.g. for MIPS, 32 bits and 32 bits)
- **Addressing modes**

Examples:

- MIPS
- RISC-V
- x86, x64 (x86_64)
- ARM-8 (likely in your smartphone)

## MIPS architecture

- CPU instructions - ISA
- CPU registers - 32 general-purpose, 4 bytes each
- Word size - 32 bits (4 bytes)
- Address size - 32 bits (4 bytes)

MIPS emulators for use in this class - 

- MARS
- SPIM

Should not use online emulators.

**Pseudo-instructions are not permitted in this class.** They do not represent actual CPU instructions.

## MIPS assembly

Example 1: `add`

```mips
add $s0, $s1, $s7 # s0 = s1 + s7
```

- Hashtag denotes a comment
- We are adding the value in register s1 with the value in s7, and putting the result in s0

MIPS tips:

- In MIPS, always one instruction per line
- Don't forget dollar sign (`$`) with register names
- Don't forget about commas
- Follow the instruction format
- No pseudo-instructions
- Beware MARS hints - MARS will allow bad code or offer pseudo-instructions, in autocomplete popups
- Must separate instruction and arguments with a space

To start we will use registers `$s0..$s7` and `$t0..$t7` (16 total registers)

Example 2: `add`

```mips
add $t6, $s1, $s0 # $t6 = $s1 + $s0
```

Example 3: `addi`

```mips
addi $t6, $s1, 4 # t6 = s1 + 4
```

- `addi` means "add immediate"
- Need to put immediate parameter last

Example 4: `addi`

```mips
addi $t6, $zero, -125 # t6 = -125
```

- `$zero` is another type of register we will use
- It is a general purpose register with zero in it
- We cannot write to or change this register because zero is so commonly used

Example 5: `sub`

```mips
sub $t6, $s1, $s0 # t6 = s1 - s0
```
