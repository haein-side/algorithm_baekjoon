import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
visited = [0 for _ in range(K+1)] # 동전의 합이 인덱스

queue = deque()
for coin in coins:
    if coin > K:
        continue
    queue.append([coin, 1]) # 동전 총합, 개수
    visited[coin] = 1

flag = False

while queue:
    val, cnt = queue.popleft() 
    
    if val == K:
        print(cnt)
        flag = True
        break
    
    for coin in coins:
        if val + coin > K:
            continue
        if visited[val+coin] == 0:
            queue.append([val+coin, cnt+1])
            visited[val+coin] = 1

if not flag:
    print(-1)