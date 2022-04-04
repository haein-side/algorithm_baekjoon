import sys
import math

n = int(sys.stdin.readline())
# 2차원 배열 선언
# 방법 1.
# a = [[0]*n]*n  # * 연산자로 2차원 배열을 만들면 얕은 복사가 실행되어 특정한 값만 변경되지 않음!

# 방법 2.
# 열은 안쪽에
# 행은 바깥쪽에
a = [[0 for j in range(n)] for i in range(n)]

d = {}

for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().split()))
    d[i] = 0

i = 0
cost = [0]*math.factorial(n-1)
while i <= n:
    for j in range(i+1, n):
        print(i, j, )
    #     if a[i][j] != 0 and d[j] != 1: # 방문할 수 있으며, 해당 도시를 방문한 적이 없을 경우
    #         # cost[i] += a[i][j]
    #         print(a[i][j])
    #         d[j] = 1
    # i += 1
            
            
print(cost)




