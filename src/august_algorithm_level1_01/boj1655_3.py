import sys
import heapq

N = int(sys.stdin.readline())
leftheap = []
rightheap = []

for i in range(N):
    n = int(sys.stdin.readline())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-n, n))
    else:
        heapq.heappush(rightheap, (n, n))
    
    if len(leftheap) > 0 and len(rightheap) > 0 and leftheap[0][1] > rightheap[0][1]:
        # leftheap의 루트와 rightheap의 루트를 바꿔주기 위해서는 push를 해주기 전에
        # 미리 pop을 해줘야 함 (그래야 바꿀 수 있음!)
        
        # 최솟값부터 힙 반환 (우선순위 순서대로 값을 꺼내올 수 있음!)
        leftnum = heapq.heappop(leftheap)
        rightnum = heapq.heappop(rightheap)
        heapq.heappush(leftheap, (-rightnum[1], rightnum[1]))
        heapq.heappush(rightheap, (leftnum[1], leftnum[1]))

    print(leftheap[0][1])