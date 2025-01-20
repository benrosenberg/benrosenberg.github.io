# Words

**A *(memory) word* is is an amount if data that the system/computer can handle in one action.**

We can think if it as a "convenient" amount of data for the computer.

In one transfer operation from RAM to a CPU register, we can move as much memory as is in one word.

People are used to 4-byte words, so they call 8-byte words "double words" sometimes. Often, the terminology used is that 4 bytes is a word; however, in this class, we recognize that this is inaccurate and that word length can vary by system.

# Buses

**A *bus* is a communication channel that can be used by *more than 2 devices*.**

(For 2 devices, we use the term *point-to-point* channel.)

Under the hood, a bus is a data channel with a bunch of wires that each transfer 1 bit (either there is voltage on the wire, or no voltage on the wire). In a 64-bit system, there would be 64 wires.

There are three types of buses we discuss:

- Data bus: data (program data, and program instructions) flows over this bus.
- Address bus: memory addresses flow over this bus. When the CPU reads from or writes to RAM, it needs to pass the memory address to read from with it. This comes via the address bus.
- Control bus: when the CPU interacts with RAM, it needs to tell RAM whether it is reading or writing. This read/write indicator comes via the control bus.

When people use the term "system bus", they mean a combination of all three of these buses.

# CPU clock

**The *CPU clock* is a device that generates synchronization pulses/signals.** 

When this signal is received, each CPU component does one unit of work.

For example, registers are only updated when the CPU clock signal is received.

We can think of the CPU clock as being the conductor of an orchestra, keeping tempo among CPU components.

## Frequency

**We say *CPU frequency* is the number of signals that the CPU clock can issue in a single second.**

In other words, CPU frequency = # CPU clock cycles / second.

We measure CPU frequency in Hertz (Hz). (We'll go over this and other units of measurement once we reach the performance part of the course.)

*side note - RAM does not work on the same frequency as the CPU; it is synchronized with the CPU in another way.*

# Program counter

We said previously that the CPU is constantly spinning in a "machine cycle" - fetch, decode, execute, write back. We also said previously that the CPU has a special register for program instructions.

The address of the next instruction is stored in the *program counter*.

**The *program counter* is a register inside the CPU that stores the address of the *next* instruction to execute.**

The address of the next instruction itself is also known as the program counter.

Programs end with a special halt instruction that returns control to the OS.

Once the CPU orders instruction reading, the CPU immediately puts the next instruction's address in the program counter.

In the case of MIPS, which we will see later, the program counter is immediately incremented by 4.

# Machine language and programming languages

## Machine language

We mentioned that in the "fetch" step of the machine cycle, the CPU gets instructions from RAM. 

**This instruction is a CPU instruction, written in what is known as *machine language*.**

(Instructions are not written in C++, or assembly - just machine language.)

Machine language is always just a bunch of zeroes and ones. (However, answering as much on an exam will result in no credit.)

In MIPS, a machine language instruction will be a group of 4 bytes.

## Programming languages - history and process

At first, all programs were written in machine language. 

Next, assembly language was created, to make writing machine code easier.

Eventually, we created high-level programming languages which are compiled into machine code by *compilers*.

**A *compiler* is a program that translates a programming language into machine code.**

Compilers convert source code into machine language. Then, this ("executable") file can be fed into the CPU.

(To see an example of a computer in which programs are written in machine code, look up the Altair 8800.)

The compilation process is as follows:

- Write CPP and header file
- Compiler translates into machine language - binary executable
- Program is run
  - Program is loaded into RAM
  - CPU executes program from RAM

An executable file is not typically readable by a text editor - it just looks like garbage because it attempts to interpret it as ASCII.

### Compilers vs. interpreters

There are two (general) models of program execution: compilation, and the use of an interpreter.

An *interpreter* does not turn the source code directly into machine code. Instead, it is a program that runs on the CPU, and takes source code/a script and does what the script says to do.