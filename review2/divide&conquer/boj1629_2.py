import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

even = b // 2 # a의 제곱 수인 것을 나눠야 할 때
if not b%2: # b가 홀수일 때
    odd = 1
else:
    odd = 0

answer = 1

for i in range(even):
    answer *= a*a % c

if odd > 0:
    answer *= a % c

print(answer % c)


