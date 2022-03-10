import sys

def sol(H, W, N):
    n = N // H
    s = N % H
    b = ""
    if s != 0:
        if n + 1 < 10:
            b = "0" + str(n+1)
        else:
            b = str(n+1)
    else:
        b = str(n)
        s = H
    return (str(s) + b)
    

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    
    print(sol(H, W, N))