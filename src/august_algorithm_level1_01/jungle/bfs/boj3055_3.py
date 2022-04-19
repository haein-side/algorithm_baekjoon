from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == '.' and c[nx][ny] == 0:
                        c[nx][ny] = c[x][y] + 1
                        q.append([nx, ny])
                    elif a[nx][ny] == 'D':
                        print(c[x][y])
                        return
            qlen -= 1
        water()

    print("KAKTUS")
    return

def water():
    qlen = len(wq) # 물이 있는 곳의 개수
    while qlen: # qlen이 0이 아닐 때까지
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == '.':
                    a[nx][ny] = '*'
                    wq.append([nx, ny])
        qlen -= 1

n, m = map(int, input().split())
a = [list(map(str, input())) for _ in range(n)] # a라는 리스트에 지도 넣음
c = [[0]*m for _ in range(n)]
q, wq = deque(), deque() # q: 고슴도치의 위치, wq: 물이 있는 곳

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S': # 고슴도치가 있는 곳
            x1, y1 = i, j # 고슴도치의 처음 위치
            a[i][j] = '.' # '.'으로 만들어줌
        elif a[i][j] == '*':
            wq.append([i, j]) # 물이 위치한 곳은 wq에 추가해줌 

water() # 먼저 물을 이동시킴
bfs(x1, y1) # 고슴도치를 이동시킴