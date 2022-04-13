import sys

T = int(sys.stdin.readline())

def bsearch(target):
    start = 0 # 검색대상이 B이므로 B의 인덱스를 start, end
    end = M - 1
    
    answer = -1
    
    while start <= end:
        mid = (start + end) // 2
        
        if target <= B[mid]:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid + 1
    
    return answer

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = sorted(list(map(int, sys.stdin.readline().split())))
    
    sum = 0
    for j in A:
        a = bsearch(j)
        if a != -1:
            sum += a
    print(sum)