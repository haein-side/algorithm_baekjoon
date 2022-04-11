# 이코테 - 그리디 알고리즘 
# p99 1이 될 때까지
import sys

n, k = map(int, sys.stdin.readline().split())

cnt = 0
while True:
    if n == 1:
        break
    if n % k == 0: # n이 k로 나눠 떨어진다면 (수 // k)로 업데이트 <- K로 최대한 많이 나눌 수 있게 하는 게 최적의 해 보장
        n = n // k
        cnt += 1
    else: # n이 k로 안 나눠 떨어진다면 (수 - 1)로 업데이트
        n -= 1
        cnt += 1

print(cnt)