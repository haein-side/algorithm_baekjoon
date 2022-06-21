from collections import deque
import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
road = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    road[a].append(b)
    road[b].append(a)

for i in range(n+1):
    road[i].sort()

visited = [False] * (n+1)

def dfs(i):
    visited[i] = True
    print(i, end = " ")
    for j in road[i]:
        if visited[j] == False:
            dfs(j)

dfs(v)

print()
visited = [False] * (n+1)

ans = []
def bfs(i):
    q = deque([i])
    visited[i] = True
    ans.append(i)
    while q:
        v = q.popleft()
        # print(v, end = ' ')
        for i in road[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                ans.append(i)

    print(' '.join(list(map(str, ans))))

bfs(v)