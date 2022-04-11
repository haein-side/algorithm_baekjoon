import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
que = PriorityQueue()
for i in range(N):
    n = int(sys.stdin.readline())
    que.put(n) # 힙에 n을 넣어줌
    nque = que
    print("que 사이즈", que.qsize())
    print("nque 사이즈", nque.qsize())
    print(que.get())
    print(que.get())
    # print(nque.get())
    # nque = que
    # for j in range(i//2):
    #     print(nque.get())
    # print(nque.get())