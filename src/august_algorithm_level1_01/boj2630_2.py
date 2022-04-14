import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

wcnt = 0
bcnt = 0

def sol(n, x, y): # n : 현재 변의 길이, x: 현재 좌표의 행 위치, y : 현재 좌표의 열 위치
    global wnct, bcnt
    
    wtmp = 0
    btmp = 0
    
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+1] == 1:
                btmp += 1
            else:
                wtmp += 1
    
    if wtmp == n*n:
        wcnt += 1
        return
    elif btmp == n*n:
        bcnt += 1
        return
    else:
        sol(n//2, x, y)
        sol(n//2, x, y + n//2)
        sol(n//2, x + n//2, y)
        sol(n//2, x + n//2, y + n//2)         

sol(N, 0, 0)

print(wcnt)
print(bcnt)