#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    tmp = []
    for i in range(3):
        for j in range(3):
            tmp.append(s[i][j])
    
    magic = []
    for a in range(1, 10):
        for b in range(1, 10):
            if set([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a]) == set(list(range(1, 10))):
                magic.append([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a])
    
    tmpres = float('inf')
    for i in range(len(magic)):
        tmpsum = 0
        for j in range(9):
            if magic[i][j] != tmp[j]:
                tmpsum += abs(tmp[j]-magic[i][j])
        if tmpres > tmpsum:
            tmpres = tmpsum
    
    return tmpres
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
