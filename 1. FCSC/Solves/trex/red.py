lst = ['aefg','adef','acdfg','adef','abdeg','abcdef','abdeg','abdegh']

res = ''

for w in lst:
    if 'd' in w:
        res += '1'
    else:
        res += '0'
    if 'c' in w:
        res += '1'
    else:
        res += '0'
    if 'b' in w:
        res += '1'
    else:
        res += '0'
    if 'a' in w:
        res += '1'
    else:
        res += '0'
    if 'e' in w:
        res += '1'
    else:
        res += '0'
    if 'f' in w:
        res += '1'
    else:
        res += '0'

    res += '1'

    if 'g' in w:
        res += '1'
    else:
        res += '0'
    if 'h' in w:
        res += '1'
    else:
        res += '0'

print(res)
print(len(res))
