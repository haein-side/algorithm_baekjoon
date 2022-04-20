from collections import deque
import sys

T = int(sys.stdin.readline())

for i in range(T):
    V, E = map(int, sys.stdin.readline().split())  # V: 정점의 개수 | E: 간선의 개수
    node = [[] for i in range(V+1)] # 0번째 노드는 비워두기
    visited = [0] * (V+1)

    for j in range(E):
        a, b = map(int, sys.stdin.readline().split())
        node[a].append(b)
        node[b].append(a)
    
    def bfs(i):
        queue = deque()
        queue.append(i)
        # 현재 노드 방문 처리
        visited[i] = 1
        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 원소 하나를 뽑아 출력
            v = queue.popleft()
            color = visited[v] # 인접 노드 보기 전 노드의 색깔을 color 변수에 담아줌 (그 전에 색칠했던 게 무슨 색인지 아는 법)
            for k in node[v]:
                if visited[k] == 0 : # 인접 노드를 방문한 적이 없을 경우
                    queue.append(k)
                    visited[k] = -color # 인접 노드 보기 전 노드의 색깔과 반대로 줌 (이분 그래프는 인접한 정점이 같은 색이면 안 되므로)
                elif visited[k] == 1: # 인접노드에 방문한 적이 있을 경우, 색깔이 1일 때
                    if color == visited[k]:
                        return False
                elif visited[k] == -1:
                    if color == visited[k]:
                        return False
        
        return True
    
    # bfs(1) # 시작노드를 1로 하고 한 번만 호출하면 되나? - 안됨!
    # 노드 하나씩 bfs를 호출해야 함 : 여러 개의 사이클이 있을 수 있기 때문!
    for e in range(1, V+1):
        if not visited[e]: # 방문한 정점이 아니라면, bfs 수행
            result = bfs(e) # 
            if result == False:
                print("NO")
                break
    else:
        print("YES")