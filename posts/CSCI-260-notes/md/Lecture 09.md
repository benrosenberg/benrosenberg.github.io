
# MIPS assembly continued

`subi` instruction does NOT exist - we can just use `addi` with a negative immediate value for the same result

- Adding an extra instruction to the CPU requires adding extra physical circuitry to the CPU, so it is not desirable
- If we can get away with using one instruction multiple ways that is good

For exams, expectation is that we memorize all MIPS instructions - no cheatsheet will be given

#### Example 1: Convert the following piece of C++ code to MIPS

```cpp
var++;
```

We are given that the value of `var` is stored in `$s3`.

---

Answer:

```mips
addi $s3, $s3, 1 # var++
```

Note - class requirement is that the `++` instruction should store the result in the same register.

#### Example 2: Convert the following piece of C++ code to MIPS

```cpp
var = 2 - var; // value of var is in $t1
```

---

Answer:

```mips
addi $s0, $zero, 2 # put 2 in register s0
sub $t1, $s0, $t1 # t1 = s0 - t1 -> var = 2 - var
```

#### Example 3: Convert the following piece of C++ code to MIPS

```cpp
var = var + (25 - var) // var in s6
```

Do NOT simplify this expression. In general our MIPS translation should just be copying whatever is in the C++ code blindly.

---

Answer:

```mips
addi $s0, $zero, 25 # put 25 in register s0
sub $s1, $s0, $s6 # s1 = 25 - var
add $s6, $s6, $s1 # var = var + s1
```

Also, when asked to comment on this, should comment on every line (or almost every line)

#### Example of a forbidden pseudo-instruction

Correct way:

```mips
addi $s0, $zero, 7
```

Incorrect way: 

```mips
li $s0, 7
```

## MIPS assembly memory operations - loads and stores

Example of memory operations in C++:

```cpp
int num = 0; // compiler reserves 4 bytes of memory in RAM
num = 20;
```

- ***Loading* - copying data from RAM to CPU register**
- ***Storing* - copying data from CPU register to RAM**

Example: `lw`

```mips
lw $t5, 2($s0)
```

`lw` means "load word" - copy 4 bytes from RAM to CPU register

- `$t5` - destination register
- `$s0` - base register - parens indicate to treat it as an address
- `2` - offset

The address read from in this line is `$s0 + 2`.

**If the offset is zero, we must specify this explicitly, e.g. `0($s0)`.**

