## Functions (cont.): `jal` and `jr`

JAL:

- Tool to jump to function code: `jal`
- The return address gets stored in `$ra` when the `jal` instruction is run
- JAL stands for "jump and link" - the linking here being the save of the return address in ra

JR:

- Tool to return to the original postion: `jr` (i.e., `jr $ra`)
- `$ra` - general purpose register, stands for "return address"

To mark a function, use a label as we have seen before

Argument and return (value) registers:

- Registers `$a0, $a1, $a2, $a3` are general purpose registers, supposed to be used to hold arguments in function calls
- Registers `$v0, $v1` are general purpose registers, supposed to be used to hold return values of function calls

Example:

Convert the following code. The first parameter is in `$a0`, second parameter is in `$a1`. Answer should be placed in `$v0`.

```c++
int sum(int a, int b) { return a + b; }
```

Solution (MIPS):

```mips
sum:
    add $t0, $a0, $a1 # a+b
    add $v0, $zero, $t0 # and place in return register
    jr $ra

...

# function usage

addi $s0, $zero, 8
addi $a0, $zero, 4
addi $a1, $zero, 5
jal sum
add $t1, $v0, $s0
```

In memory, there may be a "halt" instruction before function code space so that functions are not executed except by jumping directly to them:

```mips
# ...program code...

HALT

func1: 
    ...
    jr $ra

func2:
    ...
    jr $ra
```

## Function calling conventions

But what if registers used in a function are storing things outside the function? Then the registers will be overwritten, because registers are global variables. For instance, in the previous example, if instead of `$s0` we had set `$t0` to some value, it would have been overwritten during the function call.

Solution: function calling conventions.

- "caller" - piece of code that calls a function
- "callee" - piece of code that is called

Convention:

- a function can use s-registers, but the function must guarantee that values of all s-registers before and after the function call are the same
- a function may use t-registers without any limitations

Note:

- ALL functions must follow the above conventions.
- These rules apply to all general-purpose registers, not just s- and t-registers
  - See the green page in the textbook appendix for information on the responsibility of register preservation

In this class, we should assume that any function we are given (e.g. on an exam) follows the function calling convention correctly.

