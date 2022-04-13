import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

a = 1
while True:
    if K <= a * a:
        break
    a += 1

arr = []

for i in range(1, a + 1):
    for j in range(1, a + 1):
        arr.append(i * j)

arr = sorted(arr)

def bsearch(target):
    start = 1
    end = K

    while start <= end:
        mid = (start + end) // 2
        
        if mid < K:
            start = mid + 1
        elif mid > K:
            end = mid - 1
        else:
            return arr[mid]

print(bsearch(K))