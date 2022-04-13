import sys

N = int(sys.stdin.readline())
b = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())

def bsearch(target):
    start = 0
    end = b[-1] # 상한액을 기준으로 함
    
    while start <= end:
        mid = (start + end) // 2 # 현재 상한액
        sum = 0
        for i in b:
            if i > mid:
                sum += mid
            else:
                sum += i
        
        if sum <= m:
            answer = mid
            start = mid + 1
        elif sum > m:
            end = mid - 1
            
    return answer

print(bsearch(m))