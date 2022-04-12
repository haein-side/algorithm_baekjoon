import sys

N, K = map(int, sys.stdin.readline().split())
level = sorted([int(sys.stdin.readline()) for i in range(N)])

def bsearch(level):
    start = 0
    end = level[-1] + K
    
    while start <= end:
        mid = (start + end) // 2 # 팀 목표 레벨
        sum = 0
        for i in level:
            if i < mid:
                sum += mid - i
        
        if sum > K: # 충족되어야 하는 레벨이 K 보다 크면 mid가 작아져야 함
            end = mid - 1
        elif sum <= K:
            start = mid + 1
            answer = mid
    
    return answer


print(bsearch(level))