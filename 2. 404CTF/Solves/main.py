import time

from Crypto.Util.number import getStrongPrime, inverse, getRandomRange
from secret import flag


def encrypt( public_key, pt ):
    N, e = public_key
    return pow(pt, e, N)


def decrypt( public_key, private_key, ct ):
    N, e = public_key
    return pow(ct, private_key, N)


def gen_key( nb_bits ):
    p = getStrongPrime(nb_bits)
    q = getStrongPrime(nb_bits)
    N = p * q
    e = 65537
    d = inverse(e, (p - 1) * (q - 1))
    return ((N, e), d)


def gen_benchmarks( public_key, private_key, f):
    for i in range(200):
        r = getRandomRange(2, N)
        t = time.time()
        ct = encrypt(public_key, r)
        t_int = time.time() - t
        pt = decrypt(public_key, private_key, ct)
        t2 = time.time() - t
        check = (pt == r)
        f.write(
            f'input: {hex(r)}\nencrypted: {hex(ct)}\ntime to encrypt: {t_int}\ntime to decrypt: {t2 - t_int}\nmandatory_check: {check}\n\n')

#f = open("datatest.txt", 'w')
#public_key, private_key = gen_key(1024)
#print(private_key)
#N,e = public_key
#gen_benchmarks(public_key, private_key, f)
#encrypted_flag = encrypt(public_key, flag)

#f.write(f'N: {hex(N)}, e: {hex(e)}\n')
#f.write(f'cipher: {hex(encrypted_flag)}')
#f.close()


pkey = 2893002039448894649820364572885772634061465772398158256296983992308430123952544854031729037310544141143850184713483716531669336701896622447233386380482905079577677122665973168219510730467537671402308243987423017825927569443513459516369701962426033527139542971233622623271448071332114773070823824079358341711772829175239628123729333010635619082905056944891511946540812365379505934355333017719932881045780648830280555406686335626250702728338656507227570111162592192903334712542736412189290412308782190814862998128202776170293893243091446162835153058186140544860997070826237722184195491499800230824938948067019956941937

N = int( "0x950b1f4bf9830751e536d1a28957fe4ef45786b7e1f9753091b5f87862417499339e46f8c3fe3f37c29f710f2457e8c2975a72457b67fb1a66ba6370619450f2fb2d3939b5e9dcc03deb530da4378569e174220a9a90327414fa2f0055284c3f9ddc93f636d4d3ad9c78d0a4057b731386f9ad5b297daa75835321c97f1447d479d2d4a9814793edaea4e1c5c842c26d94d7462abbea8e2a5f3b71d50f3c20e0d25655358e277938903973205e185db42193b1b393da55c864d4356d1b6c2b36741c0e5e43b58678f094742849c43da17081ccc76de355a377d8791449e57105bcbe8baac3e491a3123fb159f212d36583d286318941ea3103b0120a6bbb874b", base=16)

e = int( "0x10001", base = 16)

pk = (N, e)

enc = int( "0x2bb17b9bb388bbcf233833f36697749e2e3f26a3d6ba10e0f48369992a83f8294d6130ac8703ec24d611f03ef097d910a10ae07f306d5506e45e6888a3ba8352d66746e3a17fda43ed036f1b7344a6d13c51392745e889d366e157bfa8f8ab1dbf635b25efb81c89e64e2431ff7b13c8c13e04340b1d4018146179d33a01225f9ce621b58169233b3818937731f830e35aa750208d4f5a32fcbc3dbe17a7f901295e4fd52969291e051b03172b85e800121f81ea9774f78c8b43b26e9caf23a139401da3a8d005935a1a4fdb3402d805e63636f8dce93a52360188462e566abcc004b4ca3125107ac08b33baf575ff492538573607ce3c30be9d7ad2416d665f", base=16)

print(decrypt(pk, pkey, enc))
