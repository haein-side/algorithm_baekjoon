# 메모리 초과
import sys
import itertools

n, s = map(int, sys.stdin.readline().split())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))

m = sorted(m, reverse = True)
m = list(itertools.combinations(m, s))    
result = []

minus = [[0 for j in range(len(m[0])-1)] for i in range(len(m))] # 이차원 배열 선언

for i in range(len(m)):
    for j in range(len(m[i])-1):
        minus[i][j] = m[i][j]-m[i][j+1]
    
# print(minus)

for i in range(len(minus)):
    result.append(min(minus[i]))

print(max(result))