# python3 -m pip install pycryptodome
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

print("Enter your password")
password = input(">>> ").encode()
h = HMAC.new(password, digestmod = SHA256)
h.update(b"FCSC2022")

iv = get_random_bytes(16)
k  = SHA256.new(password).digest()
c  = AES.new(k, AES.MODE_CBC, iv = iv).encrypt(pad(open("flag.txt", "rb").read(), 16))
r = {
	"iv": iv.hex(),
	"c": c.hex(),
	"h": h.hexdigest(),
}
open("output.txt", "w").write(json.dumps(r))
