

# MIPS assembly - Loops and Conditionals (jumps and branches)

## Jump instruction - `j` - "unconditional"

```mips
j LABEL # jump to LABEL
```

#### Example 1: Infinite loop

```mips
L1: add $s0, $s1, $s2
    add $s3, $s4, $s5
    j L1
```

- After a jump instruction, the next one to execute is the labeled one.
- The jump instruction places the address of the labeled instruction into the program counter.
- Labels exist in Assembly code only - when assembled, labels are replaced with the address of the labeled instruction.

## Conditionals/branching - `BEQ` and `BNE`

```mips
BEQ $t0, $t1, LABEL # "branch on equal" - if t0 = t1, then go to LABEL
BNE $t0, $t1, LABEL # "branch on not equal" - if t0 != t1, then go to LABEL
```

Only jump to label if condition is satisfied.

#### Example 2: Convert the following C++ code to MIPS

```cpp
for (int i = 0; i != 10; i++)
    // a is an int with value in $s0
    // keep a in $s0
    a++;
```

---

Answer:

We know we can translate `a++` like this:

```mips
addi $s0, $s0, 1 # a++
```

Now we need to do the rest of the for-loop:

```mips
        addi $t7, $zero, 0 # t7 has the value of i
        addi $t6, $zero, 10 # put 10 in t6
START:  beq $t7, $t6, EXIT # check loop condition
        addi $s0, $s0, 1 # a++ - loop body
        addi $t7, $t7, 1 # i++
        j START # back to loop start
EXIT:   ... # no need to fill in anything after EXIT label
```

## Conditionals - `SLT`, `SLTI`, `SLTU`, and `SLTIU` instructions

`SLT` stands for "set on less than":

- "setting" a register means setting it to 1
- "clearing" a register means setting it to 0

```mips
slt     $t0, $t1, $t2   # is t1 < t2 true?
slti    $t0, $t1, 234   # is t1 < 234 true?
sltu    $t0, $t1, $t2   # unsigned ver. of slt
sltiu   $t0, $t1, 234   # unsigned ver. of slti
```

For `sltu` and `sltiu`, the comparisons are **unsigned** - treat values of `$t1` and `$t2` as unsigned integers when doing comparison.

*Note: there is no "greater-than" instruction, everything can be done with `beq`/`bne` and `slt` and friends.*

#### Example 3: Convert the following C++ code to MIPS

```cpp
if (var < 10)
    var++; // value of var is in $s6
```

---

Answer:

We know we can translate `var++` like this:

```mips
addi $s6, $s6, 1 # var++
```

Conditional:

```mips
slti $t7, $s6, 10 # var < 10? if so put 1 in t7
beq $t7, $zero, EXIT # if var not < 10, skip
addi $s6, $s6, 1 # var++
EXIT:
```

#### Example 3: Convert the following C++ code to MIPS

```cpp
// value of a is in s6
// value of var is in s2
if (10 < a)
    var++;
```

---

Answer:

```mips
addi $s0, $zero, 10 # put 10 in s0
slt $s1, $s0, $s6 # 10 < a?
beq $s1, $zero, EXIT # exit if 10 not < a
addi $s2, $s2, 1 # var++
EXIT:
```
