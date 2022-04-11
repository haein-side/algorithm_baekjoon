# 이코테 - 그리디 알고리즘 
# p96 숫자 카드 게임
import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)] # 2차원 배열 (행렬 선언)
tmp = []

for i in range(n):
    tmp.append(min(arr[i]))

print(max(tmp))


