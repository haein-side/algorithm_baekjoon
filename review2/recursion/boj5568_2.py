# 풀이 2. by 백트래킹
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
li = []
checked = [0 for _ in range(n)]
answer = [] # k개 다 뽑았을 때 answer에 지금까지 쌓인 것 append해줘야
card = list(int(input()) for _ in range(n))
temp = '' # 중간 답안

def dfs(depth):
    if depth == k:
        answer.append(''.join(map(str, li)))
        return
    for i in range(n):
        if checked[i] == 0: # 아직 방문한 적이 없을 때
            li.append(card[i])
            checked[i] = 1
            dfs(depth+1)
            li.pop()
            checked[i] = 0

dfs(0)

print(len(set(answer)))