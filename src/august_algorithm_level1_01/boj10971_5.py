import sys

n = int(sys.stdin.readline())

# 2차원 배열 : 각 인덱스는 노드, 그 안의 원소는 다른 노드를 가는 데에 드는 비용
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

# minCost는 최소비용을 비교해줘야 하므로 처음엔 무한대로 설정
minCost = float('inf')
visit = [False for _ in range(n)]

def dfs(start, cur, cost):
    global matrix, minCost, visit
    
    if start == cur and visit.count(False) == 0:
        minCost = min(minCost, cost)
    
    # n개의 노드이므로 for i in range(n)
    for i in range(n):
        # 노드 0부터 n-1까지 인접노드를 한바퀴 돎
        if matrix[cur][i] != 0 and visit[i] != True:
            visit[i] = True
            # 상향식 분석으로 봤을 때, cost에 matrix[cur][i]가 계속 쌓임! (누적됨)
            dfs(start, i, cost+matrix[cur][i])
            # 재귀가 끝났을 때 전역변수인 visit[i]를 False로 초기화해둬야 다음 인접노드 돌 때 잘 돎
            visit[i] = False
            # 재귀가 끝나면 다음 코드가 실행되므로 False를 하나씩 실행해주면서 모두 False로 만들어줌!
    
dfs(0, 0, 0)
print(minCost)
