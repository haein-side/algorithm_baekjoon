import sys

N = int(sys.stdin.readline())
card = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
tlist = list(map(int, sys.stdin.readline().split())) 

def bsearch(target):
    start = 0
    end = len(card) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if target == card[mid]:
            return 1
        elif target < card[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return 0

answer = []
for i in tlist:
    answer.append(bsearch(i))
    
print(*answer)