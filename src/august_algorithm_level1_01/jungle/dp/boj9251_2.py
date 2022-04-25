import sys
input = sys.stdin.readline

x = [0] + list(input().rstrip()) # strip()은 양쪽 공백 삭제, rstrip()은 오른쪽 공백 삭제
y = [0] + list(input().rstrip())

# 2차원 배열 선언
lcs = [[0 for col in range(len(y))] for row in range(len(x))] 

# 구해야 하는 것
# lcs[len(x)-1][len(y)-1]

# 점화식
# 두 값이 같으면 lcs[i-1][j-1] + 1
# 두 값이 다르면 max(lcs[i-1][j], lcs[i][j-1])
# lcs[i][j]는 문자열 x, y 각각의 i, j번째 글자까지 최장 공통 부분 문자열의 길이

for i in range(1, len(x)):
    for j in range(1, len(y)):
        if x[i] == y[j]: # x[i]는 x의 i번째 글자, y[i]는 y의 j번째 글자
            lcs[i][j] = lcs[i-1][j-1] + 1 # x[i]와 y[i]가 일치해서 길이를 1 늘려줘야 하므로 1을 더해줌
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
       
print(lcs[len(x)-1][len(y)-1])