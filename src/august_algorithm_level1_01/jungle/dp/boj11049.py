import sys
input = sys.stdin.readline
n = int(input())
matrix = [[0,0]] # [[0, 0], [5, 3], [3, 2], [2, 6]]
p = [0] + [0 for _ in range(n+1)] # [0, 5, 3, 2, 6]

# 행렬 정보
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# p 값
p[1] = matrix[1][0]
for i in range(2, n+1):
    p[i] = matrix[i][0]
p[n+1] = matrix[n][1]

# dp 테이블
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 정리
# 예제
# 3
# 5 3
# 3 2
# 2 6

# 내가 구해야 하는 것 : 입력으로 주어진 행렬의 순서를 바꾸면 안 되고 주어진 순서 그대로 dp[1][3]을 구해야 한다.
# dp[i][j]가 의미하는 것 : i행렬부터 j행렬까지의 최소 곱셈 연산 횟수
# 예제로 보았을 때 i는 1, j는 3으로 고정됨

# 점화식 : dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1])
# 여기서 k는 i부터 j-1이하의 값

for a in range(n-1, 0, -1):
    for b in range(1, a+1):
        for c in range(1, b+1):
            dp[b][b+1] = min(dp[b][c] + dp[c+1][j])
