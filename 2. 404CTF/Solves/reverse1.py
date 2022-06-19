def tour1(password):
    string = str("".join( "".join(password[::-1])[::-1])[::-1])
    print("string", string)
    l = [ord(c) for c in string]
    print("t1", l)
    return l


def tour2(password):
    print("t2", password)
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(password[password.index(password[i])] + password[password.index(password[ i + 1 %len(password)])])
        password.pop(password.index(password[i]))
        i += int('qkdj', base=27) - int('QKDJ', base=31) + 267500
    return new

def tour3(password):
    print("t3", password)
    mdp =['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(len(password)):
        mdp[i], mdp[len(password) - i -1 ] = chr(password[len(password) - i - 1] + i % 4),  chr(password[i] + i % 4)
    return "".join(mdp)

def t3(mdp):
    passw = [ str(i) for i in range(len(mdp))]
    for i in range(len(passw)):
        passw[i], passw[len(passw) -i -1] = ord(mdp[len(passw) -i -1]) - i%4, ord(mdp[i]) - i%4
    print("t3t", passw)
    return passw

def t2(new):
    passwd = []
    for i in range(len(new)//2):
        passwd.append(new[i*2])
    print("t2t", passwd)
    return passwd

def t1(l):
    print("t1t", l)
    passwd = [chr(c) for c in l[::-1]]
    passwd = "".join(passwd)
    return passwd

mdp = "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"

b = t1(t2(t3(mdp)))
print("b", b)
