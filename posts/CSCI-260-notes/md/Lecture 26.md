## Control unit and control lines (cont.)

Note: in the textbook there is a table (see below) that has information on control circuitry (do NOT need to memorize for final exam).

Additional terminology:

- "deasserted" => set to 0
- "asserted" => set to 1
- "signal name" => e.g., "RegDst", or "ALUSrc"
- "don't care condition" => if we don't care about the value on a control line, we write "X" instead of 0 or 1. 
  - Note that this matters for the exam - if we write 0 or 1 instead of X, even if it isn't used, points will be deducted.

Control line functions:

- MemRead: controls whether Data Memory component performs memory reading or not
  - Supplies 1 through control line if so, otherwise 0
  - e.g. for ADD instruction, send 0
- MemtoReg: leads to Multiplexor (MUX)
  - if 0 then sends ALU result to register file
  - if 1 sends memory content (from data memory read) to register file
- RegDst: determines where to write
  - If asserted, register to write comes from Instr[15:11] (shorthand for bits 15 through 11 of the instruction)
  - If deasserted, comes from Instr[20:16]
- MemWrite: whether to write to memory or not
- ALUSrc: control second output of ALU
  - immediate value vs. register
  - immediate value is 1, register is 0
- RegWrite: controls whether register is written to in register file
  - Basically just the "write enable" input from earlier
- ALUOp: linked to ALU control unit

ALU control unit:

- 2 inputs:
  - First input: Instr[5:0] (function field)
    - Recall: R-type instructions have opcode 0 and are differentiated by the function field

Example: Control line values for `sw` instruction

```mips
sw $s0, 12($t6)
```

Control lines for the above instruction will have the following values:

- RegDst: X ("don't care")
- Branch: 0
- MemRead: 0
- MemtoReg: X ("don't care")
- ALUOp: 00 (see table for ALU operations in previous lecture)
- MemWrite: 1
- ALUSrc: 0
- RegWrite: 0


The "don't care" conditions are relevant in the following example scenarios:

- RegWrite is 0, so we are not writing
  - Therefore, RegDst should be "X" because choosing which register "not" to write to is meaningless
- MemRead is 0, so we are not reading from memory
  - Therefore, MemtoReg should be "X" because choosing how to use the memory value we are "not" reading from is meaningless

# CPU design approaches

1. Single-cycle: 1 instruction per cycle
   - Bad because instructions take different time to execute
   - Can only choose one clock speed, so every clock cycle needs to take at least as long as the longest-running instruction (ends up being very slow)
2. Multi-cycle: different instructions take different numbers of cycles
   - Good because we can differentiate between short-running and long-running instructions
   - But we can do better - still some inefficiencies
3. Pipelining
   - Idea: start working on next instruction while processing previous instruction