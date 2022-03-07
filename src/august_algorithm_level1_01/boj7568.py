import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x,y])

ans = ""
for i in range(n):
    count = 1
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count += 1
    ans = ans + str(count) + " "

print(ans.strip())