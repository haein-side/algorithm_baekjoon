# 성곤님 코드
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())
maze = [list(map(int,list(input().strip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# print(maze)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

heap = [(0,0,0)]
while heap:
    # heap을 쓰는 이유
    # 최소의 개수로 검은 방을 지나가야 하기 때문에 
    # 비용이 적은 흰색 방을 최대한 많이 거쳐가야 함!
    # 그래서 내가 갈 수 있는 곳 중 비용이 적은 방들을 먼저 탐색해주기 위해 (= 벽을 덜 뿌시기 위해)
    # heappop()을 이용해서 비용 적은 흰 방부터 탐색을 들어감!
    # 이후에 비용이 높은 방인 검은 방을 탐색해주는 것!
     
    (cnt, cx, cy) = heapq.heappop(heap)

    if cx == n-1 and cy == n-1:
        print(cnt)
        break  
    maze[cy][cx] = cnt
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            # 흰색인 경우
            if maze[ny][nx] == 1 and not visited[ny][nx]: 
            # visited 쓰는 이유 : 최단 거리는 최단 거리가 갱신되면 남겨둬야 함 (더 더할 필요 없음)
                heapq.heappush(heap, (cnt, nx, ny))

            # 회색인 경우
            elif maze[ny][nx] == 0 and not visited[ny][nx]:
                heapq.heappush(heap, (cnt+1, nx, ny))

            visited[ny][nx] = True
            