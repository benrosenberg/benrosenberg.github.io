

# MIPS assembly - more exercises

#### Example 1: Convert the following C++ code to MIPS

```cpp
// var is an unsigned int
// address of var is in $s3
do  {
    var -= 20;
} while (var > 100);
```

---

Answer:

**Version 1**:

```mips
    addi $s0, $zero, 100 # put 100 in s0
    lw $s1, 0($s3) # load var into s1

LOOP: 
    addi $s1, $s1, -20 # var -= 20
    sltu $s2, $s0, $s1 # check if 100 < var (UNSIGNED)
    beq $zero, $s2, END # if var <= 100 ($s2 = 0), break
    j LOOP # 100 < var, so continue looping

END:
    sw $s1, 0($s3) # update var
```

**Version 2**:

```mips
    addi $s0, $zero, 100 # put 100 in s0
    lw $s1, 0($s3) # load var into s1

LOOP: 
    addi $s1, $s1, -20 # var -= 20
    sltu $s2, $s0, $s1 # check if 100 < var (UNSIGNED)
    bne $zero, $s2, LOOP # if var < 100 ($s2 = 0), continune looping

    sw $s1, 0($s3) # update var
```

Notes:

- Since `var` is an unsigned *int*, we don't need to use an unsigned instruction - there is no `lwu` instruction because there is no padding necessary as an int is 4 bytes, which is the same size as a register
- We could load and store in each loop, but it is more efficent to load once pre-loop and store once post-loop.
- Version 2 is more efficient because we save one instruction by checking for inequality instead of equality.

#### Example 2: Convert the following C++ code to MIPS

```cpp
// value of a is in s0
switch (a) {
    case 0:
        // case 0...
        break
    case 1:
        // case 1...
        break
    default:
        // default case...
}
```

---

Answer:

**Version 1**:

```mips
    beq $zero, $s0, CASE_0 # if a is 0, go to case 0
    addi $s1, $zero, 1 # put 1 in s1
    beq $s1, $s0, CASE_1 # if a is 1, go to case 1
    j DEFAULT # if a is something else, go to default case

CASE_0: 
    # case 0...
    j EXIT

CASE_1:
    # case 1
    j EXIT

DEFAULT:
    # default case

EXIT: ...
```

**Version 2**:

```mips
CASE_0:
    bne $zero, $s0, CASE_1 # a != 0 so jump to case 1
    # case 0...
    j EXIT

CASE_1:
    addi $s1, $zero, 1 # put 1 in s1
    bne $s1, $s0, DEFAULT # a != 1 so jump to default case
    # case 1...
    j EXIT

DEFAULT:
    # default case...

EXIT: ...
```