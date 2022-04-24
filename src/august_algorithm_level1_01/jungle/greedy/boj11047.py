import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0 for _ in range(n)]

for i in range(n-1, -1, -1):
    coins[i] = int(input())

i = 0
res = 0
while True:
    if coins[i] <= k:
        res += k // coins[i]
        k = k - k // coins[i] * coins[i]
    i += 1
    if k == 0:
        break
print(res)