import sys
import heapq
N = int(sys.stdin.readline())
leftheap = []
rightheap = []

for i in range(N):
    num = int(sys.stdin.readline())
    
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-num, num))
    else:
        heapq.heappush(rightheap, (num, num))
    
    # leftheap의 루트가 rightheap의 루트보다 크면 중간값이 안되므로 바꿔줘야 함!
    if len(leftheap) > 0 and len(rightheap) > 0 and leftheap[0][1] > rightheap[0][1]:
        left = heapq.heappop(leftheap)
        right = heapq.heappop(rightheap)
        
        heapq.heappush(leftheap, (-right[1], right[1]))
        heapq.heappush(rightheap, (left[1], left[1]))
        
    print(leftheap[0][1])