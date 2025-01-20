# Operations on bits (bitwise operations)

Example:

```c++
int pixel {102345}; // stores some pixel color value
```

to make darker by a factor of 2, we just need to halve each byte component - would need to use bitwise operations

Example: to change the way devices work, we may want to flip bits in a register

`srl`, `sll` - shift right logical and shift left logical

Example (srl, sll):

```mips
srl $t1, $t0, 2 # shift 2 bits right
sll $s0, $s5, 3 # shift 3 bits left
```

-   bits that "fall off" are discarded
-   "empty" bits as a result are filled with zeroes

Example (c++):

```c++
int a,b;
b = a << 2;
b = a >> 1;
```

Example (shifting one position left):

```
0000 0011 = 3
0000 0110 = 6
0000 1100 = 12
0001 1000 = 24
```

each shift multiplies by 2

Example (shifting one position right):

```
1100 = 12
0110 = 6
0011 = 3
0001 = 1
```

each shift does int division by 2

Note: `srl` and `sll` are preferred to mult or div when using powers of 2, because they are much more simple (and efficient)

Other binary operations:

|                | and    | or     | xor    |
| -------------- | ------ | ------ | ------ |
| symbol         | `&`    | (pipe) | `^`    |
| `0101 op 0110` | `0100` | `0111` | `0011` |

"pipe" above is `|` (markdown table formatting makes it hard to write)

Example:

```mips
and $t4, $t3, $t1 # t4 = t3 & t1
andi $t4, $t3, 6 # t4 = t3 & 6
```

also, `xori` and `ori` operators exist.

Other things to do with bit operations:

- flip a specific bit
- set a specific bit
- clear a specific bit
- get a specific bit

When counting bits, we go right to left, counting from 0 to 31. (again, in this course we assume 32-bit word size.)

So for example, bit #2 of a number is the 4s place (in general, bit X is the $2^X$ place)

Example:

```mips
# s0 holds value. goto L1 if bit #2 is set.

addi $t0, $zero, 4 # create mask
and $t1, $s0, $t0 # apply mask to s0
bne $t1, $zero, L1 # goto L1 if bit was set
```

in this case the `and` will zero out the value if bit #2 was not set and give the result of the mask if it is set, so the `bne` will only jump if the bit was set.

(note: in above code, the addi and and could have been collapsed into a single `andi` instruction, but was separated for pedagogical purposes.)

Example: set bits 4 and 6 in s0

```mips
# create mask - 01010000
addi $t0, $zero, 0x50 # create mask
or $s0, $s0, $t0 # apply mask
```

> note - in above code, could have used `ori` operator as well.

> note - in the above code, we use 0x50 because this is the shorter hex version of 01010000. it is easy to convert - split into groups of 4 binary digits and convert each to hex. for example, 0101 is 5 and 0000 is 0, so we get 0x50.


