import base64
from bitstring import BitArray
from pwn import *
from time import sleep

b64alp = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/0123456789"""

def clean(st):
    res = ""
    for i in st:
        if i not in b64alp:
            if i == "х":
                res += "x"
            elif i == "с":
                res += "c"
            elif i == "у":
                res += "y"
            elif i == "А":
                res += "A"
            elif i == "В":
                res += "B"
            elif i == 'К':
                res += "K"
            elif i == 'Н':
                res +="H"
            elif i == 'Т':
                res += "T"
            elif i == 'а':
                res += "a"
            elif i == 'е':
                res += "e"
            elif i == 'о':
                res += "o"
            elif i == 'р':
                res += "p"
        else:
            res += i

    res += "="*(len(res)%4)
    return res

p = remote("challenge.404ctf.fr", "30117")

glob = b""

for i in range(6):
    p.recvline().decode()
text = p.recvline()
text = text.decode().split(" : ")[1].strip()
text = clean(text)
text = base64.b64decode(text)
glob += text
text = BitArray(text).bin
p.sendline(bytes(text, "utf-8"))

for i in range(249):
    try:
        text = p.recvline()
        print((i/249)*100)
    except:
        sleep(5)
    while len(text.decode().split(" : ")) == 1:
        try:
            text = p.recvline()
        except:
            sleep(5)
    text = text.decode().split(" : ")
    text = text[1].strip()
    text = base64.b64decode(clean(text))
    glob += text
    text = BitArray(text).bin
    p.sendline(bytes(text, "utf-8"))
a = True
while a:

    try:
        print(p.recvline())
    except:
        a = False

f = open("res.mp3", "wb")
f.write(glob)
