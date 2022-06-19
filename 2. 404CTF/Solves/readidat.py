#!/usr/bin/env python3
from PIL import Image
import zlib
from binascii import unhexlify

with open("stage3.png", 'rb') as f:
    hexData = f.read().hex().strip()

chunks = []

PNGHeaderHex = hexData[0:16]

cursor_0 = 16

read = True
while read:

    start = cursor_0
    stop = cursor_0+(4*2)
    cursor_0 = stop

    chunkDataLengthHex = hexData[start:stop]
    chunkDataLength = int(chunkDataLengthHex,16)

    start = cursor_0
    stop = cursor_0+(4*2)
    cursor_0 = stop
    chunkTypeHex = hexData[start:stop]
    chunkType = bytes.fromhex(hexData[start:stop]).decode()

    start = cursor_0
    stop = cursor_0+(chunkDataLength*2)
    cursor_0 = stop
    chunkDataHex = hexData[start:stop]

    start = cursor_0
    stop = cursor_0+(4*2)
    cursor_0 = stop
    chunkCrcHex = hexData[start:stop]

    cursor_1 = 0

    if chunkType == "IDAT":
        chunks.append((chunkType, chunkDataLengthHex + chunkTypeHex + chunkDataHex + chunkCrcHex))
    elif chunkType == "IEND":
        print('Reached image end')
        read = False
    else:
        chunks.append((chunkType, chunkDataLengthHex + chunkTypeHex + chunkDataHex + chunkCrcHex))

index = [len(i[1]) for i in chunks].index(max([len(i[1]) for i in chunks]))

print(str(len(chunks)) + " chunks were found, the biggest one being n°" + str(index+1) + " with length :", len(chunks[index][1]), " and of type : ", chunks[index][0])

def construct(chunks, index):

    idatChunkHex = chunks[index][1]
    newChunksHex = PNGHeaderHex + chunks[0][1]+idatChunkHex+chunks[-1][1]

    with open("outfile", "wb") as outf:
        outf.write(bytes.fromhex(newChunksHex))


construct(chunks, index)
