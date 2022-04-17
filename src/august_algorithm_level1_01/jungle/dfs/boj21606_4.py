# 성곤님 코드

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = input().rstrip() # 1은 실내 0은 실외 | .rstrip()은 문자열 끝의 공백을 제거 
A = 'n' + A # 입력받은 문자열을 배열처럼 활용하기 위해 인덱스 맞춰줌
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


# 시작,종료가 모두 실내
# 그 외엔 전부 실외


# 방문 안 했고 실외(0)라면 dfs 방문 안 했고 실내(1)라면 +1
def dfs(now):
    visited[now] = True

    for p in graph[now]:
        if not visited[p]: # 0(실외)만 있는 경우는 모두 visited True로 처리되므로 '1'이 append 되지 않음
            if A[p] == '0': # 입력받은 문자열을 그냥 배열처럼 활용
                dfs(p)
            else:
                ans.append('1')


ans = []
for i in range(1,N+1):
    visited = [False] * (N+1)
    if A[i] == '1':
        dfs(i)

print(len(ans))