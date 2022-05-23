# import sys
# input = sys.stdin.readline

# word1 = input()
# word2 = input()

# # 잉여 행과 열을 두고 2차원 배열 선언
# dp = [[0 for col in range(len(word1) + 1)] for row in range(len(word2) + 1)]

# for i in word2:
#     for j in word1:
#         if i == j: 

import sys
input = sys.stdin.readline

x = [0] + list(input().rstrip())
y = [0] + list(input().rstrip())

lcs = [[0 for col in range(len(y))] for row in range(len(x))]
# 인덱스 값으로는 맨 끝 값이 lcs[len(x)-1][len(y)-1]에 들어감

for i in range(1, len(x)):
    # 어차피 lcs dp 테이블에 1부터 값을 넣어주므로 i-1, j-1을 계산하기 위해 넣어준 0에는 값을 넣지 않는다.
    for j in range(1, len(y)):
        if x[i] == y[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[len(x)-1][len(y)-1])