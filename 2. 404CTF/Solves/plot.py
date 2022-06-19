import matplotlib.pyplot as plt


Y=[]
with open("8vers10.txt") as src:
    for line in src.readlines():
        Y.append(line.strip())

X = [i for i in range(len(Y))]

plt.figure()
plt.scatter(X,Y)
plt.show()
