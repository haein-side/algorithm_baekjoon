import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input()) # 정점의 수
place = [0] + list(map(int, list(input().strip()))) # 1은 실내, 0은 실외
node = [[] for _ in range(N+1)] # 노드
visited = [False] * (N+1) # 방문 기록

# 간선 정보 입력
for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

# 실외와 인접한 실내의 개수 구하기
def dfs(i):
    home_cnt = 0
    for j in node[i]: # i의 인접노드 j
        if place[j] == 1: # 실내일 때
            home_cnt += 1
            continue
        else: # 실외일 때
            if not visited[j]: # 실외에 방문한 적 없을 때
                visited[j] = True
                home_cnt += dfs(j)
    return home_cnt

cnt = 0

# 인접 경로
for i in range(1, N+1):
    if place[i] == 1: # 현재 노드가 실내일 때
        for j in node[i]: # 인접노드
            if place[j] == 1: # 실내일 때
                cnt += 1
    else: # 현재 노드가 실외일 때
        if not visited[i]: # tmp로 방향이 switch된 것도 다 고려해주는 것! -> visited처리를 해줘야 중복 피할 수 있음
            visited[i] = True
            tmp = dfs(i)
            cnt += tmp * (tmp-1) 

print(cnt)
