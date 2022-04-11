import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
que = PriorityQueue()

for i in range(N):
    n = int(sys.stdin.readline())
    que.put(n) # 힙에 n을 넣어줌
    
    arr = []
    for j in range(i // 2):
        arr.append(que.get())
    tmp = que.get()
    print(tmp)
    arr.append(tmp)
    
    for k in arr:
        que.put(k)
    