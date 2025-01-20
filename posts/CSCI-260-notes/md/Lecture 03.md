Will soon send out an enrollment verification thing that Hunter requires to ensure you actually attend the course. Important to fill out otherwise you will be dropped from the course.

Office hours start next week.

# RAM in more depth

Registers were the smallest and fastest memory - in our case, about 4 bytes in size for the general purpose registers we use for MIPS assembly.

We now discuss RAM in more depth - "zoom in" on the contents.

For programmers, RAM is presented as a linear array of bytes.

\begin{figure}[H]
\begin{centering}
\includegraphics[]{images/01.jpg}
\vspace*{-10mm}
\caption{RAM}
\end{centering}
\end{figure}

*side note - in reality, not actually an array of bytes - physical limitations make this impossible (64 wires going into each byte, because of memory address sizes being 64 bit nowadays, makes this impossible or at least very inconvenient), but we can percieve it as linear. As programmers we can think using this abstraction.*

There is no way to have "empty" slots in RAM - something will always be there, whether it is zeroes or some other random value. There is no guarantee that it will be anything specific - could be anything at all.

Every byte in RAM has its own memory address.

(Note - do not confuse memory addresses and the content at those addresses.)

We will use memory addresses when working with assembly to refer to memory locations.

In Figure 1, we have 16 cells, so we need 16 different memory addresses.

$16 = 2^4$, so we need 4 binary digits in order to represent all memory addresses.

> Question: How much memory can we address with 32-bit addresses?
>
> Answer: $2^{32} \approx 4$GB of memory.

*side note - this limit based on memory address size is only the case for byte-addressable memory. For word-addressable memory (not commonly used) there could be more than the above-described limit.*

> Question: What is the minimum size of memory addresses needed for 2000 bytes of RAM?
>
> Answer: Since $2^{10} = 1024$ and $2^{11} = 2048$, this requires 11-bit addresses.

The formula for the above type of problem is $\lceil \log(N) \rceil$ where $N$ is the number of bytes of RAM desired.

Usually, when dealing with memory addresses, numbers in hexadecimal (hex) are used (i.e., [1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]). This is because they are convenient to use - shorter than binary representations and easy to convert to binary and back.

Easy to convert hex and binary - just convert groups of 4 bits at a time.

> Example converting hex to bin: 3DF corresponds to 0011 1101 1111

(The above example is spaced out for readability, and zero-padded on the left for consistency.)

> Example converting bin to hex: 1010111 corresponds to 87

We also deal with (contiguous) chunks of data of size greater than 1 byte.

For these larger chunks, the memory address used to refer to them is the first (smallest) address in the chunk.

# Programming languages and memory

All (high-level) programming languages have convenient ways to interact with memory: **variables**

Variables do not exist at a hardware level - just a tool that high-level programming languages have to conveniently refer to memory addresses.

> Example: `char symb = 'a';`

C++ first finds a place in RAM to store this new character. It will find some 1-byte chunk of RAM to use in this case.

Then, every time a user interacts with `symb`, it will use that memory address.

\begin{figure}[H]
\begin{centering}
\includegraphics[]{images/02.jpg}
\vspace*{-10mm}
\caption{\texttt{char symb = 'a';}}
\end{centering}
\end{figure}

> Example: `int var = 5;`

\begin{figure}[H]
\begin{centering}
\includegraphics[]{images/03.jpg}
\vspace*{-10mm}
\caption{\texttt{int var = 5;}}
\end{centering}
\end{figure}

> Example: `var++;`

For `var++`, the CPU does the following:

1. the CPU asks for 4 bytes from address C (1100 in binary)
2. the CPU does arithmetic to add 1 to this int
3. the CPU stores the result back into RAM

Note how the above steps correspond to the Fetch, Execute, and Writeback steps of CPU execution. (Decode is saved for later in the course.)

We cannot write/modify RAM directly: it has to be modified in the CPU, and then written/copied back to RAM.

The compiler stores memory addresses in a symbol table and retrieves them when the variable is used.

Post-compilation, variables are turned into memory addresses.

*side note - for each program, the OS creates virtual memory so that programs do not overlap memory addresses in RAM. Addresses that we see from our program's perspective are not actual physical addresses - instead, they are virtual RAM addresses. this is convenient for us because we don't need to think about anything besides our use of RAM (i.e., we don't need to think about other programs running at the same time.)*

# Pointers

> Example: `int *ptr;`

A pointer variable is just a variable.

The *size* of a pointer depends on the architecture - e.g. for a 32-bit architecture, the size of a pointer is 4 bytes (32 bits); for a 64-bit architecture, it would be 8 bytes.

In our example, presume that the size of a pointer is one byte. 

> Example: `ptr = &var;`

(recall `var` is stored at address 1100, and contains the integer 5.)

So, now `ptr` stores 1100.

The size of a pointer is the size of a memory address.

\begin{figure}[H]
\begin{centering}
\includegraphics[]{images/04.jpg}
\vspace*{-10mm}
\caption{\texttt{ptr = \&var;}}
\end{centering}
\end{figure}

The *int* part of the `int *ptr` is actually unnecessary because the size of pointers is always the same - it is just there for type safety. In fact, we can even have `void *ptr` if we want - we just need to explicitly cast it to some type before dereferencing.

**For exams, know the following C++ type sizes:**

type      | typical size
----------|--------------------------------------------
char      | 1 byte
short     | 4 bytes
int       | 4 bytes
long      | at least size of int, typically 4 bytes
long long | 8 bytes usually outside of embedded systems
float     | 4 bytes
double    | 8 bytes
bool      | 1 byte (byte is the min size in RAM)

*side note - for memory efficiency (at the cost of minor speed degradation), C++ vectors of booleans will use on average 1 bit per bool.*

These types also have unsigned versions - same size as signed versions, but are only positive. Just expressed in different ways (2's complement vs. bare binary number)


