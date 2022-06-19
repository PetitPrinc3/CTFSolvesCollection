

img = open('flag.png', 'rb')

hexdata = img.read().hex()

garb1 = "2a4700080000000000a0720480000000000000"
hexdata = hexdata.replace(garb1, "")
garb2 = "ac0032c618638c31c618638c2971"
hexdata = hexdata.replace(garb2, "")

with open('res.png', 'wb') as outf:
    outf.write(bytes.fromhex(hexdata))
