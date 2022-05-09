import sys
input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())))
m = int(input())
origin = list(map(int, input().split()))
target = sorted(origin)

def binary_search(t):
    start = 0
    end = len(num)-1

    while (start <= end):
        mid = (start + end) // 2
        if num[mid] < t:
            start = mid + 1
        elif num[mid] > t:
            end = mid -1
        else:
            return 1

    return 0

for t in origin:
    print(binary_search(t))