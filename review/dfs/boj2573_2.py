# 민성님 코드
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ice_list = [] # 0보다 큰 ice_list의 좌표 
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4)]
maps = [] # 전체 지도
# [[0, 0, 0, 0, 0, 0, 0], [0, 2, 4, 5, 3, 0, 0], [0, 3, 0, 2, 5, 2, 0], [0, 7, 6, 2, 4, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j]:
            ice_list.append((i,j))
    maps.append(tmp)

def dfs(x, y):
    if visited[x][y]:
        return
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if maps[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)
        

year = 0
while ice_list:
    visited = [[False] * M for _ in range(N)] 
    del_list = []

    for x,y in ice_list:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not maps[nx][ny]:
                cnt += 1
        if maps[x][y] - cnt <= 0:
            del_list.append((x,y))
        else:
            maps[x][y] -= cnt
    
    for x,y in del_list:
        maps[x][y] = 0
    ice_list = list(set(ice_list) - set(del_list))

    year+=1

    cycle = 0
    for x,y in ice_list:
        if not visited[x][y]:
            dfs(x,y)
            cycle += 1
    if cycle >= 2:
        break

if ice_list:
    print(year)
else:
    print(0)