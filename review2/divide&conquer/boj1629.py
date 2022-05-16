# 1629 곱셈
# 시간초과
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
answer = a
for i in range(b-1):
    answer *= a
answer = answer % c

print(answer)