import server
import numpy as np
import base64

a = 'CAN I GET THE FLAG'
b = server.morse_encode(a).strip()
print(b)
c = server.am_encode(b)

for i in c:
	print(i)
