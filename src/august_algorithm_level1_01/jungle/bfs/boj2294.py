import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

print(coin)