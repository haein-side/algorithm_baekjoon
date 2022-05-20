import sys
input = sys.stdin.readline

n = int(input())

tile = [1, 2]

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(2, n):
        tile.append((tile[i-1] + tile[i-2]) % 15746)

    print(tile[-1])
