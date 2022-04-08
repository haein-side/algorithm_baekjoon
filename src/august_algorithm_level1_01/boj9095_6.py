import sys

t = int(sys.stdin.readline())
nlist = []
count = 0

def sol(n):
    global count
    if n == 0:
        count += 1
        return 
    if n < 0:
        return 
    
    for i in range(1, 4):
        sol(n-i)
        
for i in range(t):
    sol(int(sys.stdin.readline()))
    print(count)
    count = 0