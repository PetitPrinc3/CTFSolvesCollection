import binascii

word = []


with open("dns", "r") as dns:
    for line in dns.readlines():
        word.append(line.strip())

lst = []
w = []

for i in range(len(word)):
    if word[i] == "626567696E":
        w = []
    elif word[i] == "656E64":
        lst.append("".join(w))
    else:
        w.append(word[i])
un = []

for i in lst:
    un.append("".join(list(i)))

for i in un:
    f = open("res/"+str(un.index(i)), "wb")
    for j in range(len(i)//2):
        try:
            hexed = str(i[j*2])+str(i[(j*2)+1])
            f.write(binascii.unhexlify(hexed))
        except:
            print("e")
    f.close()
