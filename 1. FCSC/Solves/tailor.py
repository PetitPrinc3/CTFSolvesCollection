import string
import random

N = 8

def encode(pwd):
    def F(tmp):
        if tmp % 2:
            return (tmp % 26) + ord('A')
        else:
            r = tmp % 16
            if r < 10:
                return ord('0') + r
            else:
                return r - 10 + ord('A')

    a, res = 0, []
    for i in range(len(pwd)):
        P, c, S = pwd[:i], pwd[i], pwd[i+1:]
        S1, S2, T = sum(P), sum(S), sum(pwd)
        a = F((a + c) * i + T)
        res.append(a)

    return bytes(res)

def get_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length)).encode()

P = []

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

i1, i2, i3, i4, i5, i6, i7, i8 = 0,0,0,0,0,0,0,0
i = 0



with open("wordlist.txt", "w") as outp :
    for l1 in range(i1, len(alphabet)):
        for l2 in range(i2, len(alphabet)):
            for l3 in range(i3, len(alphabet)):
                for l4 in range(i4, len(alphabet)):
                    for l5 in range(i5, len(alphabet)):
                        for l6 in range(i6, len(alphabet)):
                            for l7 in range(i7, len(alphabet)):
                                for l8 in range(i8, len(alphabet)):
                                    word = alphabet[l1]+alphabet[l2]+alphabet[l3]+alphabet[l4]+alphabet[l5]+alphabet[l6]+alphabet[l7]+alphabet[l8]
                                    code = encode(word.encode())
                                    outp.write(word + "::" + str(code) + '\n')
                                    print(str(round((i/(26**8))*100, 3)) + "% - " + str(i) + "/" + str(26**8), end = '\r')
                                    i += 1
