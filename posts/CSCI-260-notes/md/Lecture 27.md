Final exam - scheduled for 12/19/2024

- Cumulative - mostly new questions but will have some old material as well
- 2 hours - 6:20-8:20

---

Pipelining - start working on next instruction before previous instruction is done executing.

Idea: take picture (CPU diagram) and reposition components to come in stages/layers

- Draw dotted lines between sections of diagram
- Each section gets a clock tick

As soon as first instruction moves to register file from instruction memory unit, second instruction can go to instruction memory unit.

- Leads to higher CPU component utilization
- Will not go into implementation details because of limited time
- Will not be asked to deal with pipeline diagrams on final either

## MIPS pipelining stages

1. Instruction fetch
2. Instruction decode (including control unit, and register reading)
3. Execution
4. Memory access
5. Write back

Note: in reality, there are 20-30 pipelining stages - the above is a simplified pipeline.

The more pipelining stages there are, the more efficient the CPU will be.

## Pipeline hazards

Sometimes, there are situations where pipelining malfunctions or isn't possible - these are known as **pipelining hazards**.

- Structural hazard: two instructions need the same component at the same time
  - Not an issue for MIPS
- Data hazard: can either deal with via data forwarding, or there may be no easy way out
  - Data forwarding: compiler helps with this issue by rearranging instructions (see example)
  - No easy way out: rearranging instructions may not be able to help with the issue (see example)
- Control hazard: CPU unsure where program goes next, needs to wait for program to continue executing to determine
  - Branch prediction can be used to eliminate some of the issue with this but not always accurate

Example: data and control hazards

```mips
# data hazard that can be fixed with data forwarding
# (compiler rearranging instructions)
addi $t0, $t1, 3
add $t2, $t0, $t4

# data hazard with no easy way out
lw $t0, 0($s1)
add $t2, $t0, $t4

# control hazard - will behave differently based on branch
beq $s1, $s2, L1
add $t0, $t0, $t0
sw $t0, 0($s7)
L1: addi $t0, $t0, -1
```

More terminology:

- "Pipeline bubble": waiting (stalling) for data from previous instruction
- "Pipeline stall": pipeline has to wait for instruction(s) to finish

Data forwarding:

- Method to mitigate (at least partially) inefficiencies introduced to data hazards when pipelining
- Value that next instruction needs may be ready even before that instruction has finished the rest of the pipeline
- e.g., the result from the ALU can be forwarded back to the ALU input directly

Branch prediction (aka speculative execution):

- Method of (or hardware mechanism for) mitigating control hazards
- Tries to predict which branch is taken - CPU guesses
- If guess is incorrect, CPU needs to flush pipeline
- Note: in modern CPUs, there is a complicated branch prediction unit
- Note: compilers may use "branchless programming" or alternative methods to make branches more predictable
