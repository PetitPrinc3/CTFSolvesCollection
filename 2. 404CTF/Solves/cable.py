import asciis

with open("Cable.txt", "r") as file:
    for line in file.readlines():
        numb = line.split(" ")

numb.pop()
print(numb)
print(len(numb))


res = '1'
print("res", res)

for nu in numb[1:]:
    if nu == '-1':
        res += res[-1]
    else:
        res += str((int(res[-1])+1)%2)

print(res)

res = [res[i:i+7] for i in range(0, len(res), 7)]
print(res)

fin = ''

for car in res:
    fin += str(asciis.bit_7[str(car)])

print(fin)
