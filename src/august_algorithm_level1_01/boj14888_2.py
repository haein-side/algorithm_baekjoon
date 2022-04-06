# 연산자 끼워넣기 DFS로 풀어보기
import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
plus, minus, gop, na = map(int, sys.stdin.readline().split())
minCost = 1e9
maxCost = -1e9

def dfs(depth, total, plus, minus, gop, na):
    global minCost, maxCost
    
    if depth == n: # 모든 연산 다 했을 때
        minCost = min(minCost, total)
        maxCost = max(maxCost, total)
        return # return 해줘야 재귀함수가 끝남!
    
    if plus:
        dfs(depth+1, total + nlist[depth], plus - 1, minus, gop, na)
    if minus:
        dfs(depth+1, total - nlist[depth], plus, minus - 1, gop, na)
    if gop:
        dfs(depth+1, total * nlist[depth], plus, minus, gop - 1, na)
    if na:
        dfs(depth+1, int(total / nlist[depth]), plus, minus, gop, na - 1)   

dfs(1, nlist[0], plus, minus, gop, na)

print(maxCost)
print(minCost)