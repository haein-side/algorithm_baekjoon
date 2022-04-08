import sys

t = int(sys.stdin.readline())
nlist = []

def sol(n):
    count = 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    for i in range(1, 4):
        count += sol(n-i)
        
    return count 

for i in range(t):
    print(sol(int(sys.stdin.readline())))