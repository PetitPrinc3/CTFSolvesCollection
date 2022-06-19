import sys
import numpy as np
import base64

HOST ="challenges.france-cybersecurity-challenge.fr"
PORT =2251

hello_signal = np.fromfile("signal.iq", dtype = np.complex64)

encoded_signal = base64.b64encode(hello_signal.tobytes())

c.recvuntil(b"> ")
c.sendline(encoded_signal)
print(c.recvline())
