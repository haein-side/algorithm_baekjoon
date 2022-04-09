import sys
n, m = map(int, sys.stdin.readline().split()) # n개의 줄에 m개씩 원소
a = [list(map(int, input().split())) for _ in range(n)] # 리스트 안에 리스트를 여러번 인풋 받음 (2차원 배열)

m, k = map(int, sys.stdin.readline().split())
b = [list(map(int, input().split())) for _ in range(m)]

# N(행)*M(열), M(행)*K(열) 행렬을 곱하면 N(행)*K(열) 행렬이 됨!!!
# N과 K에 대해 이중 for문을 돌면서, 벡터의 크기 M만큼 for 돌면서 
# 행벡터와 열벡터의 각 요소 곱의 더하기 값을 구해주고 결과 행렬에(2차원 리스트) 넣어주면 된다.

axb = [[0]*k for _ in range(n)]
for row in range(n):
    for col in range(k):
        e = 0
        for i in range(m):
            e += a[row][i] * b[i][col]
        axb[row][col] = e
    
for r in axb:
    print(*r)