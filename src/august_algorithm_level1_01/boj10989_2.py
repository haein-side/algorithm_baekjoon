from sys import stdin

n = int(stdin.readline())
arr = [0] * 10001
for i in range(n):
    arr[int(stdin.readline())] += 1

for i in range(len(arr)):
    if arr[i] > 0:
        for j in range(arr[i]):
            print(i)
    