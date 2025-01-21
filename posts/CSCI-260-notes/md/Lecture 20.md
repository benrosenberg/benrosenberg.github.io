## Functions, continued (example)

Example from last lecture, but we save s0 on the stack so that value is preserved across function calls:

```mips
sum:
    # save s0 on the stack
    addi $sp, $sp, -4 # make stack 4 bytes larger to save full word-sized value
    sw $s0, 0($sp) # save s0 to the stack where space was just made for it
    add $s0, $a0, $a1
    add $v0, $zero, $s0

    # restore s0 from the stack
    lw $s0, 0($sp) # restore s0 contents from the stack to s0
    addi $sp, $sp, 4 # make stack 4 bytes smaller
    jr $ra
```

### stack pointer revisited

Stack pointer - general purpose register indicating the end of the stack

Using the stack pointer in a function:

- Make stack larger by decreasing sp
- Then: use new sp as starting point, because RAM grows upwards while stack grows down
- Also: need to return stack to original state once function is over, by moving stack pointer

Note on function pointer:

- We will not use fp in this class
- There are some architectures that don't have access to fp, and only use sp

Example: multi-argument saving to the stack:

```mips
AVERAGE:
    # store s0 and s1 on stack
    addi $sp, $sp, -8
    sw $s0, 0($sp)
    sw $s1, 4($sp)

    # function body
    add $s0, $a0, $a1
    srl $s1, $s0, 1
    add $v0, $zero, $s1

    # revert s0 and s1 to pre-function call values
    lw $s0, 0($sp)
    lw $s1, 4($sp)
    addi $sp, $sp, 8
    jr $ra
```

Example: calling another function inside a function:

```mips
# issue: $ra will have been overwritten by this function call
# solution: put $ra on the stack as well!

AVERAGE:
    addi $sp, $sp, -12
    sw $s0, 0($sp)
    sw $s1, 4($sp)
    sw $ra, 8($sp)

    # function body
    add $a3, $a0, $a1
    jal DIVBYTWO # parameter in a3, result in v1
    add $v0, $zero, $v1

    lw $s0, 0($sp)
    lw $s1, 4($sp)
    lw $ra, 8($sp)
    addi $sp, $sp, 12
    jr $ra
```

Example: using t-register outside a function:

```mips
addi $t0, $zero, 8
addi $a0, $zero, 4
addi $a1, $zero, 5
addi $sp, $sp, -4 # inc stack size by 4 bytes
sw $t0, 0($sp) # preserve t0 on stack
jal SUM
lw $t0, 0($sp) # retrieve t0 from stack
addi $sp, $sp, 4 # dec stack size by 4 bytes
add $t1, $v0, $t0
```

