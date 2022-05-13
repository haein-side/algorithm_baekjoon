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
    color = paper[x][y] # 첫번째 블럭의 색깔

    for i in range(k):
        for j in range(k):
            if color != paper[x + i][y + j]:
                # 제 1사분면
                sol(k//2, x, y)
                # 제 2사분면
                sol(k//2, x, y+k//2)
                # 제 3사분면
                sol(k//2, x+k//2, y)
                # 제 4사분면
                sol(k//2, x+k//2, y+k//2)
                # return의 존재 이유
                # 제 4사분면까지 한번씩만 재귀를 돌면 항상 판단이 끝남
                # but, return이 없으면 한 번 판단할 때마다 끝까지 파고 들어서
                # 한 변의 길이가 1이 될 때까지 계속 재귀를 돌 것
                return
    
    # 4 사분면까지 다 돈 이후 동일한 색깔만 있을 때
    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return


sol(n, 0, 0)
print(white)
print(blue)