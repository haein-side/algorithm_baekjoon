import sys

def sol(H, W, N):
    x = ""
    y = ""
    if N % H != 0:
        x = str(N % H)
        if N // H + 1 < 10:
            y = "0"+ str(N // H + 1)
        else:
            y = str(N // H + 1)
    else:
        x = str(H)
        if N // H < 10:
            y = "0"+ str(N // H)
        else:
            y = str(N // H)
    return x + y
        
    

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    
    print(sol(H, W, N))