# 2630번 색종이 만들기
# 27:00

import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0 # 하얀색의 개수
blue = 0 # 파란색의 개수

def sol(k, x, y): # k 한 변의 길이 x 현재 x축 좌표 y 현재 y축 좌표
    global white, blue

    if k == 1:
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
        return

    w, b = 0, 0

    for i in range(k):
        for j in range(k):
            if paper[x + i][y + j] == 0:
                w += 1
            else:
                b += 1
    
    if w == k*k:
        white += 1
        return
    elif b == k*k:
        blue += 1
        return

    # 제 1사분면
    sol(k//2, x, y)
    # 제 2사분면
    sol(k//2, x, y+k//2)
    # 제 3사분면
    sol(k//2, x+k//2, y)
    # 제 4사분면
    sol(k//2, x+k//2, y+k//2)



sol(n, 0, 0)
print(white)
print(blue)