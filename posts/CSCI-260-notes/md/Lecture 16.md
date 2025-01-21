CPU instructions (continued)

- all instructions are 4 bytes long
- op code is always in leftmost 6 bits
- rest of instruction is interpreted based on the first (leftmost) 6 bits

to convert instruction to binary:

- use textbook appendix to look up instruction format - will be given on exams

### I-type instrs. cont.

For the immediate values in I-type instructions, need to use 2's complement to specify negative immediate values. This means that the range for immediate values is $[-2^{15}, 2^{15}]$ (the same as the range of a short int). 

Therefore, you cannot fully load large values into the register - there are "load upper immediate" instructions that we use to fill the upper half of the register (this is NOT covered in this course)

## J-type (jump) instructions

Example J-type instruction: 

```mips
j label
```

J-type instruction structure:

```plaintext
XXXXXX|XXXXXXXXXXXXXXXXXXXXXXXXXX
opcode| target address
```

We are told that for jump instructions, the opcode is 2.

## Addressing modes

26 bits is insufficient to address the entire range of RAM (we assume RAM is addressible using 32 bits), so we need to use tricks ("addressing modes")

Four different addressing modes we will cover:

- Base addressing
  - Just use offset from a register, like when loading or storing
  - Example: `lhu $s0, 4($s5)` -> address is s5 + 4
  - Limitation: there is a limitation on how large the immediate value can be, as discussed above for I-type instructions
    - Typically we don't encounter this issue, the imm. values just take advantage of already having the base address stored in a register - $2^{15}$ is around 32 to 33 KB in either direction so we are not super likely to run into issues, and if we do, the compiler will just take care of it
- PC-relative (program-counter-relative) addressing
  - Use an offset from the program counter
  - Example: `beq $t0, $t1, L1` -> address is PC + L1 $\times$ 4
  - Limitation: needs to be an address reasonably close to the program counter for this to work
    - Typically this limitation is addressed by the compiler, won't go over it in our course
  - PC-relative addressing uses the 16-bit immediate value for I-type instructions
    - We are able to slice off the last 2 bits (on the right side) because the instructions are always a multiple of 4 (provided the alignment for instructions is done correctly), saving us 2 bits
- Pseudodirect addressing
  - Like pc-relative addressing - we cut out the last 2 bits because the instructions are always a multiple of 4, and then cut off the first 4 bits so that the address fits into the 26-bit space we are given
  - Limitation: The 4 bits at the start are just taken from the PC so we can't jump super far.
    - Compiler probably addresses this issue too
- Register addressing
  - Literally just set PC to the register contents
  - Example: `jr $ra` -> set PC to contents of `$ra`
  - Limitations: none.
  - Typically used when returning from function call after calling `jal` on the level above

### Example with most of the addressing modes (just without register addressing, will see that later)

Convert the following mips code to binary, and put it at address `0x00400068`, using big-endian bit direction.

```mips
Label1:
    bne $t1, $zero, Label2
    lw $t7, -2($s0)
    add $t7, $t7, $zero
    j Label1

Label2:
    ...
```

- We note that the jump must be to address `0x00400068` because Label1 is at the start of the code
- Note that the PC keeps the address of the NEXT instruction, so to compute the distance when labeling we use the next instruction as a starting point (for e.g. the BEQ instruction)
- For the BEQ instruction, we will jump 3 instructions ahead. When we are the BEQ instruction, our PC points to the LW instruction, so jumping ahead means adding 3 to the PC.
- For the LW instruction, we need to put -2 in the immediate value. This is -1 + -1, so we just need to remove 1 from the all-ones 16-digit binary number `1111 1111 1111 1111`, which gives us `1111 1111 1111 1110` for the immediate value.

The instructions are translated as follows:

- `bne $t1, $zero, Label2`
  - `000101 01001 00000 0000000000000011`
  - opcode is 5
- `lw $t7, -2($s0)`
  - `100011 10000 01111 1111111111111110`
  - opcode is 0x23 or 35. imm value is discussed above
- `add $t7, $t7, $zero`
  - `000000 01111 00000 01111 00000 100000`
  - opcode is 0, function is 0x20
- `j Label1`
  - `000010 00000100000000000000011010`
  - opcode is 2, address is just `0x00400068` but missing the first (leftmost) 4 bits and without the last (rightmost) 2 bits due to the addressing mode

