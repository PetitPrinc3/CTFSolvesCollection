import numpy as np

img = np.array()

l = 0

for i in range(24):
    for j in range(24):
        img[i,j] = Image.open(str(l+j)+".png")

print(img)
