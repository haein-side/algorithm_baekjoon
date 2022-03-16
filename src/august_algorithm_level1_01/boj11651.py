from sys import stdin

n = int(stdin.readline())
arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, stdin.readline().split()))
    
arr = sorted(arr, key= lambda x:(x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])
