from collections import deque

n = int(input())
q = deque()
q.append((n, [n])) # 현재 수와 연산이 이루어지는 수 리스트
visited = [0]*(n+1)

while q:
    num, ans = q.popleft()
    
    if num == 1:
        print(len(ans)-1)
        print(*ans)
        break
    if not visited[num]: # 0이라면 방문 아직 안 한 것
        visited[num] = 1
        if num % 3 == 0:
            q.append((num//3, ans+[num//3]))
        if num % 2 == 0:
            q.append((num//2, ans+[num//2]))
        q.append((num-1, ans+[num-1]))