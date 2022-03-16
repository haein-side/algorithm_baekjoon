import math
from sys import stdin
n, k= map(int, stdin.readline().split())

def fac(n):
    if n > 1:
        return n * fac(n-1)
    else:
        return 1

a = fac(n)
b = fac(k)
c = fac(n-k)

print(a // (b * c))
