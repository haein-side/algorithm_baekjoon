import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

def sol(target, data):
    start = 0
    end = N - 1
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return answer
    

for i in range(M):
    print(sol(target[i], arr))
