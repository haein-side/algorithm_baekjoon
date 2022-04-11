# 이코테 - 그리디 알고리즘 
# p92 큰 수의 법칙

import sys
n, m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr, reverse = True)

answer = 0

answer = k * (m // k) * arr[0] + (m % k) * arr[1]

print(answer)