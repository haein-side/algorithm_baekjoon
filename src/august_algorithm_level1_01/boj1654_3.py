import sys

K, N = map(int, sys.stdin.readline().split())
len = [int(sys.stdin.readline()) for i in range(K)]


def bsearch(target):
    start = 1
    end = max(len)
    while start <= end:
        mid = (start + end) // 2
        
        num = 0
        for i in len:
            num += i // mid
            
        if num < target:
            end = mid - 1
        elif num >= target:
            start = mid + 1
       
    return mid
    
print(bsearch(N))