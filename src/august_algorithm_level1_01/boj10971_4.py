import sys

def dfs(start, cur, cost):
    global matrix, visit, minCost # visit는 배열, 이미 방문한 곳은 더 방문하지 못하게
    
    # 다 방문했을 때
    if start == cur and visit.count(False) == 0:
        # 방문 시 True로 바꿔주기 때문에 False가 한 개도 없으면 다 방문한 것
        # start == cur로 다시 돌아온 것 => 다 방문한 것
        minCost = min(minCost, cost) # 아예 이동하지 못했을 수도 있으므로
        # 출발점과 현재 위치가 같다면 cost를 minCost와 비교해서 더 작은 값을 넣어줌
    
    for i in range(n):
        # matrix[cur][i]는 현재 노드에 인접한 노드 i로 가는데 드는 비용
        # 이코테와 달리 0과 인접한 모든 노드를 dfs하면서 모든 경우의 수를 탐색
        # 자기 자신의 값은 0이므로 다음 i(노드)로 넘어감
        if not matrix[cur][i] == 0 and not visit[i]: # 방문되지 않았다면
            visit[i] = True
            dfs(start, i, cost+matrix[cur][i]) # 인접노드 i를 cur로- 현재위치 업데이트(즉, 인접한 노드로 움직이는 것)
            visit[i] = False # 이해 X

n = int(input())
            
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

# dfs
minCost = float('inf')
visit = [False for _ in range(n)]
dfs(0, 0, 0)

print(minCost)