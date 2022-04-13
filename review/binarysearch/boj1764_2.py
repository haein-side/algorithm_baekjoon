import sys

N, M = map(int, sys.stdin.readline().split())
hear = sorted([sys.stdin.readline().strip() for i in range(N)])
see = [sys.stdin.readline().strip() for i in range(M)]

def bsearch(target): # 검색대상 : hear, 검색 타겟 : see
    start = 0
    end = len(hear) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if hear[mid] < target:
            start = mid + 1
        elif hear[mid] > target:
            end = mid - 1
        else: 
            return hear[mid]
        
    return None
        
        

answer = []
for i in see:
    a = bsearch(i)
    if a is not None:
        answer.append(a)

answer = sorted(answer)
        
print(len(answer))

for i in answer:
    print(i)    
