# 민성님 코드
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

places = list(map(int, list("0"+input().strip())))

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N+1)

for _ in range(1, N):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

cnt = 0

def dfs(v)->int:
    home_cnt = 0
    # 실외에 근접한 실내 개수 세기
    for i in adj_list[v]:
        if places[i] == 1:      # 실내이면 카운트 + 1
            home_cnt += 1
            continue
        else:                   # 실외이면 한 번 더 돌기
            if not visited[i]:
                visited[i] = True
                home_cnt += dfs(i) 
                # 이 부분에서 재귀를 돌음!
                # 그리고 재귀를 돌 때 home_cnt 는 다시 0으로 초기화 되고 원래 있던 4에 더해짐 (원래 돌던 코드는 이 라인에 멈춰있음)
    return home_cnt

for i in range(1, N+1):
    if places[i] == 1:              # 실내 - 실내 인 경우에만 더해줌
        for j in adj_list[i]:
            if places[j] == 1:
                cnt+=1
    else:                          # 실외인 경우
        if not visited[i]:
            visited[i] = True
            tmp = dfs(i)
            cnt += tmp * (tmp - 1)

print(cnt)