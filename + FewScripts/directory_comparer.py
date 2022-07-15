#!/bin/env/python3

import filecmp
import os
import sys
import pyfiglet

if len(sys.argv) < 2:
    print("Usage : python compare.py path1 path2")
    exit()

path1 = sys.argv[1]
path2 = sys.argv[2]

def compare(file1, file2):
    if filecmp.cmp(file1, file2, shallow = False):
        return ""
    else :
        return file2

def main(path1, path2):

    files1 = []
    for r, d, f in os.walk(path1):
        tmplen = 0
        for file in f:
            files1.append(os.path.join(r, file))
            length = (abs(tmplen - len(os.path.join(r, file)) - 15) - (tmplen - len(os.path.join(r, file)) - 15))//2 + 1
            print('\033[92m' + "File available : " + os.path.join(r, file) + " "*length, end = '\r')
            tmplen = len(os.path.join(r, file))

    files2 = []
    for r, d, f in os.walk(path2):
        tmplen = 0
        for file in f:
            files2.append(os.path.join(r, file))
            length = (abs(tmplen - len(os.path.join(r, file)) - 15) - (tmplen - len(os.path.join(r, file)) - 15))//2 + 1
            print('\033[92m' + "File available : " + os.path.join(r, file) + " "*length, end = '\r')
            tmplen = len(os.path.join(r, file))

    print('\n\033[92m ===== Done =====\n\n')

    uniques = []
    files1_ = []
    files2_ = []

    for file in files1:
        name2 = os.path.join(path2, file.split(path1)[-1])
        if name2 not in files2:
            uniques.append(file)
        else:
            files1_.append(file)

    for file in files2:
        name1 = os.path.join(path1, file.split(path2)[-1])
        if name1 not in files1:
            uniques.append(file)
        else:
            files2_.append(file)

    files1_.sort()
    files2_.sort()

    differences = []
    tmplen = 0

    for a in range(len(files1_)):

        file1 = files1_.pop()
        file2 = files2_.pop()

        length = (abs( tmplen - (len(file1) + len(file2) + 4) ) - ( tmplen - (len(file1) + len(file2) + 4) ))//2 + 1
        print('\033[93m' + "Processing : " + file1 + " & " + file2 + " "*length, end = '\r')
        tmplen = len(file1) + len(file2) + 4

        if file1.split("/")[-1] == file2.split("/")[-1]:
            file = compare(file1, file2)
            if file != "":
                differences.append(file)
        else:
            print('\n\033[91m' + "error : " + file1 + "    " + file2)

    print('\n\033[92m ===== Done =====\n\n')

    with open("output2.txt", "w") as output:
        for file in uniques:
            print('\033[91m' + 'Unique : ' + file)
            output.write('u:' + file + '\n')

        for file in differences:
            print('\033[93m' + "Differ : " + file)
            output.write('d:' + file + '\n')

    print('\n\n\033[92m' + "See full report : output.txt")

main(path1, path2)
