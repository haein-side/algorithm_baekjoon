# 최단거리가 나오지 않는 풀이

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [[] for _ in range(N+1)]
for i in range(1,N+1):
    miro[i] = list(input().rstrip())
    miro[i] = [-1] + list(map(int, miro[i])) 
       
visited = [[False for _ in range(M+1)] for _ in range(N+1)]

def up(i, j):
    if 1 <= i-1 <= N and 1 <= j <= M and miro[i-1][j] == 1 and not visited[i-1][j]:
        return True
    return False

def down(i, j):
    if 1 <= i+1 <= N and 1 <= j <= M and miro[i+1][j] == 1 and not visited[i+1][j]:
        return True
    return False

def left(i, j):
    if 1 <= i <= N and 1 <= j-1 <= M and miro[i][j-1] == 1 and not visited[i][j-1]:
        return True
    return False

def right(i, j):
    if 1 <= i <= N and 1 <= j+1 <= M and miro[i][j+1] == 1 and not visited[i][j+1]:
        return True
    return False

n = 1

def start(i, j) : # i: 현재 행 위치, j: 현재 열 위치
    global n
    if i == N and j == M:
        return
    
    if up(i, j):
        n += 1
        visited[i][j] = True
        start(i-1, j)
    if down(i, j):
        n += 1
        visited[i][j] = True
        start(i+1, j)
    if left(i, j):
        n += 1
        visited[i][j] = True
        start(i, j-1)
    if right(i, j):
        n += 1
        visited[i][j] = True
        start(i, j+1)

start(1, 1)
print(n)