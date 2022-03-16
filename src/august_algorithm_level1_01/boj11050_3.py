import math
from sys import stdin
n, k= map(int, stdin.readline().split())

def fac(a):
    result = 1
    for i in range(1, a+1, 1):
        result *= i
    return result

a = fac(n)
b = fac(k)
c = fac(n-k)

print(a // (b * c))
