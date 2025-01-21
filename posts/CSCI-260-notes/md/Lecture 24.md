### Reminder item: Logic units

Adder: used to add two 32-bit numbers together

![Adder](2025-01-20-20-55-23.png)

Arithmetic Logic Unit (ALU): used for all arithemtic operations (subtraction, addition, etc.)

![ALU](2025-01-20-20-56-45.png)

Multiplexor (MUX): select one of 2 (or more) values to use

![MUX](2025-01-20-20-59-41.png)

From textbook page 246

## CPU design diagrams

![Textbook p.246: high-level MIPS CPU diagram](2025-01-20-21-02-22.png)

![Textbook p.247: mid-level MIPS CPU diagram](2025-01-20-21-03-53.png)

![Textbook p.265: low-level MIPS CPU diagram](2025-01-20-21-04-40.png)

Note: For final exam, need to be able to read and understand CPU design schematics/diagrams like those in the above images.

**Datapath**: 

- Hardware that performs actual work
- Circuitry that helps with instruction execution in CPU
- e.g., ALU, etc.
- Marked by black lines in above diagrams

**Control circuitry**:

- Configures datapath for instruction that CPU needs to execute
  - Disables unnecessary components, enables useful components, etc.
- Marked by blue lines in above diagrams

## CPU components

**Instruction memory component**:

- Stores instruction being executed
- Asks for 4-byte instruction from RAM, at the address that it got from the program counter


