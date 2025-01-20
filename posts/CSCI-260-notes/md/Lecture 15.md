## More bitwise operation examples

Example: clear bits #4 and #6

```mips
addi $t0, $zero, -81 # create the mask
and $s0, $s0, $t0 # apply mask
```

here, we are creating the following mask:

> `1111111110101111`

This is the same as $-1-64-16 = -81$

The logic is that if we `and` with a 1, it will be unchanged, but if we `and` with a 0, it will get cleared.

The way to generate the mask is:

- Start with -1
- For each bit with number X (e.g., bit #4) you want cleared, subtract $2^X$
  - for example, for bit #4 it would be $-1-2^4 = -1-16 = -17$

Example: invert bits 4 and 6

```mips
addi $t0, $zero, 80 # create mask
xor $s0, $s0, $t0 # apply mask
```

The mask created here is the inverse of the one above (we can tell because it is negated and decremented, which is how 2's complement works):

> `0000000001010000`

an `xor` with 1 flips the value of a bit:

- 0 xor 1 = 1
- 1 xor 1 = 0

and an `xor` with 0 leaves the value alone:

- 0 xor 0 = 0
- 1 xor 0 = 1

this allows our mask to work as desired.

# CPU instructions

"How large are CPU instructions?" -> MIPS instructions are 4 bytes long, or 32 bits.

different types of instructions - R-type, I-type, and J-type

## Example: R-type instruction (add)

R-type instructions have the following structure:

```plaintext
XXXX XX|XX XXX|X XXXX|XXXX X|XXX XX|XX XXXX
opcode | rs   | rt   | rd   |shift | func
```

above, bits are split into groups of 4, but the way the bits are used does not use this 4-bit grouping, instead using the following:

- 6 bits opcode (e.g., for R-type instructions, this is 0 - distinguish using function field)
- 5 bits rs
- 5 bits rt
- 5 bits rd
- 5 bits shift amt
- 6 bits function

rs, rt, and rd have the following meanings:

- `rs` : register source
- `rt` : register target (this is where the result is written for I-type, or immediate, instructions, if relevant)
- `rd` : register destination (this is where the result is written for R-type instructions)

each register has a numeric name, from 0 to 31. the 5 bits for each register are sufficient to identify each register because $2^5 = 32$.

Example CPU instruction translation: 

```mips
add $s0, $t0, $t1
```

We can use a table to verify the following numeric IDs for each of the registers above:

- s0 - 16 = 10000
- t0 - 8 = 01000
- t1 - 9 = 01001

We are also given in a table that the format for the `add` instruction is:

> `add rd, rs, rt` <- so, the `rd` register gets the destination and the rs and rt registers are the inputs

Also from the table we are told that the value of the function field for `add` is `100000`, and the shift amt is `00000`.

This gives us the following for `add $s0, $t0, $t1`:

> `0000 00|01 000|0 1001|1000 0|000 00|10 0000`

The breaks are added to show which parts are the operator, registers, etc.

Without breaks or spacing it looks like this:

> `00000001000010011000000000100000`

A little difficult to debug.

## Example: I-type instruction (addi)

I-type instructions have the following structure:

```plaintext
XXXX XX|XX XXX|X XXXX|XXXX XXXX XXXX XXXX
opcode | rs   | rt   | immediate value
```

For `addi`, we are told that the opcode is 8, or 001000 in binary.

We will translate the following instruction:

```mips
addi $s1, $t7, 6
```

This is as follows, using the table for register numbers and converting 6 to the binary 110 and padding with zeros:

> `001000 01111 10001 0000000000000110`

again, we split the above up by opcode, registers, and immediate value for visibility.