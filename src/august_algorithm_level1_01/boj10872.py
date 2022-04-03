import sys

n = int(sys.stdin.readline())

def fac(n):
    if n == 0:
        return 1
    else:
        a = 0
        if n == 1:
            return 1
        a = n * fac(n-1)
        return a
    
print(fac(n))