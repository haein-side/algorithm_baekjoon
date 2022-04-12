import sys

N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for i in range(N)]

while K >= 1:
    arr[arr.index(min(arr))] = arr[arr.index(min(arr))] + 1
    K -= 1

print(min(arr))
