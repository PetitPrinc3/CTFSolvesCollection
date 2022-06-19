from io import BytesIO
from binascii import hexlify, unhexlify

disk0 = open('disk0.img', 'rb').read()
disk1 = open('disk1.img', 'rb').read()
disk2 = bytes([ d0^d1 for d0, d1 in zip(disk0, disk1)])

data = []

for i in range(min(len(disk0), len(disk1), len(disk2))):
    if i%3 == 0:
        data.append(disk0[i])
        data.append(disk1[i])
    elif i%3 == 1:
        data.append(disk0[i])
        data.append(disk2[i])
    else:
        data.append(disk1[i])
        data.append(disk2[i])
    print(i, end='\r')

bts = bytearray(data)

with open('raid', 'wb') as outf:
    outf.write(bts)
