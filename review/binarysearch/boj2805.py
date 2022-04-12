import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

def bsearch(target):
    start = 0
    end = max(tree)

    while start <= end:
        mid = (start + end) // 2 # 절단기 높이
        
        sum = 0
        for i in tree:
            if i >= mid:
                sum += i - mid
        
        if sum < target: # 더 많이 잘라줘야 -> 절단기 길이 작아져야
            end = mid - 1
        elif sum >= target: # 더 적게 잘라줘야 -> 절단기 길이 길어져야
            start = mid + 1
            answer = mid
            
    return answer


print(bsearch(M))