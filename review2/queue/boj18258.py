from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
    
def sol(order):
    tmp = order.split()
    if tmp[0] == 'push':
        q.append(tmp[1])
    elif tmp[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif tmp[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    elif tmp[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif tmp[0] == 'size':
        print(len(q))
    elif tmp[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

for _ in range(n):
    sol(input())
