# 1번과 연결된 노드의 개수?
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

net = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

cnt = 0

def dfs(x):
    global  cnt
    visited[x] = True
    cnt += 1
    for i in net[x]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(cnt-1)