import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins = sorted(coins, reverse = True)
i = 0
res = 0
while True:
    if k == 0:
        break
    if k >= coins[i]:
        res += k // coins[i]
        k -= coins[i] * (k // coins[i])
    i += 1

print(res)

