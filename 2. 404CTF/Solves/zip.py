import zipfile
import tarfile
import os

file = tarfile.open("flag2500.tar.gz")

for i in range(2499):
    file = tarfile.open(file)
file.extractall()
