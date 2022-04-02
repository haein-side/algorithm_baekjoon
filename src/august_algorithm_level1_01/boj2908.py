import sys 

a, b = sys.stdin.readline().split()

a = a[::-1]
b = b[::-1]

print(max(a,b))