import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

wcnt = 0 # 흰색 개수
bcnt = 0 # 파란색 개수

def sol(n, x, y): # n: 현재 변의 길이, x: 현재 좌표의 행 위치, y: 현재 좌표의 열 위치
    global wcnt, bcnt
    
    wtmp = 0
    btmp = 0
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] == 1:
                btmp += 1
            else:
                wtmp += 1
    if wtmp == n*n: # 흰색으로만
        wcnt += 1
        return
    elif btmp == n*n: # 파란색으로만
        bcnt += 1
        return
    else : # 같은 색으로만 이루어져 있는 게 아닐 때
        sol(n//2, x, y)
        sol(n//2, x, y + n//2)
        sol(n//2, x + n//2, y)
        sol(n//2, x + n//2, y + n//2)   
        

sol(n, 0, 0)

print(wcnt)
print(bcnt)