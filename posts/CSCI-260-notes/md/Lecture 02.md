Reading from a hard disk is *not* random access - could take longer or shorter depending on the location of the item we want to read on the disk.

# Cache

**Note:** most of this info is not going to show up on exams, just need to know the definition of cache.

RAM is slow, and is the bottleneck of computer performance.

To make average CPU-RAM interactions faster, cache memory was introduced.

The cache is close to the CPU. **The *cache* is a memory device used to make average CPU-RAM interactions (that is, reads and writes) faster.**

Cache is relatively small and fast.

When the CPU needs something from RAM, it checks cache first. If not found, it goes to RAM.

When something new is delivered to the CPU from RAM, it is copied to cache first, as well as its neighbors in RAM. (Usually around 64 to 128 bytes are copied to cache at a time - depends on the CPU model.)

Cache stores the most recently accessed pieces of memory, removing the least recently used items over time. (This is known as an LRU cache.)

We can think of cache + RAM as being a black box, the CPU just thinks it's accessing RAM and has no knowledge of the cache's existence.

Caching is used widely, not just in hardware but also in browsers and many other places where reading again is expensive.

The goal for CPU manufacturers when designing cache memory devices is to maximize the *hit ratio*, or the proportion of time that the CPU finds what it is looking for in cache rather than in RAM.

But the cache is a mechanical device - it's not complex, so typically it will use a simplification of the LRU cache algorithm that approximates it.

We said previously that RAM is random access, meaning it takes on average the same amount of time to access any piece of memory in RAM. However, in practice, we want to stay in the same areas of RAM, so we minimize cache misses (because the cache loads contiguous chunks of memory into RAM all at once, including neighbors). For this reason, iterating over arrays is faster than iterating over linked lists in practice, despite both having O(n) iteration runtime complexity: arrays are cache-friendly, as they are literally contiguous blocks of memory themselves.

Cache specifically influences *average* speed of CPU-memory interactions, rather than all interaction speeds - there are still cache misses, which will take the same time as without cache.

Modern cache memory can have up to 90% hit ratio - very good, only 1/10 attempted read/write operations from CPU result in a cache miss and have to go to RAM.

Cache also speeds up RAM write, but it's a more complicated process than reading - the cache may delay writing to RAM for the sake of efficiency, or use other tricks.

Size hierarchy:

- CPU registers are on the order of bytes
- Cache memory is on the order of kilobytes
- RAM is on the order of megabytes to gigabytes
- Storage is on the order of gigabytes and higher

# Memory volatility and storage devices

Ram is *volatile*. 

**We say a memory device is *volatile* if the device loses all data when power is lost.**

To get around the volatile property of RAM, we have storage devices.

**We define *storage devices* as large memory devices that use non-volatile technology.**

Common storage devices: HDD, SSD

- HDD - large, cheap, slow. Possibly spinning disks, not random access
- SSD - faster than HDD, but still slow compared to RAM
- Other storage devices - flash drives, CDs/optical storage devices, tape (tape is still used in practice for backups)

Regardless of storage type, all storage is still significantly slower than RAM.

Because of this, file reading/writing to storage is typically done on another thread, or separately from other program execution.

Throughput of storage devices may be comparable to that of RAM (e.g. 6GB/s for SATA), but the delay until data is recieved is significant regardless.

# Executable files

**An *executable* file is a file that contains program code.**

When you click on an icon on your computer, you tell the PC (operating system) to start an executable. 

Then, it **copies the code from the executable file on the hard disk into RAM, and begins executing the program**.

Executable files do not have all data necessary for program execution - other data could be retrieved during program execution from the filesystem, network calls, etc.

# ROM

The last memory device we will cover is ROM.

**ROM stands for *read-only memory*. ROM is a separate memory chip/device that stores programs necessary for the computer to boot up/start.**

When the PC starts, the CPU starts reading and executing from ROM.

ROM is also sometimes called *firmware*.