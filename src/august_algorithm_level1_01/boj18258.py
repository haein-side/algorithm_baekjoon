from collections import deque
import sys

n = int(sys.stdin.readline())
d = deque()
def sol(n):
    global d
    if "push" in n:
        d.append(n.split()[1])
    if "pop" in n:
        if len(d) > 0:
            print(d.popleft())
        else:
            print(-1)
    if "size" in n:
        print(len(d))
    if "empty" in n:
        if len(d) > 0:
            print(0)
        else:
            print(1)
    if "front" in n:
        if len(d) > 0:
            print(d[0])
        else:
            print(-1)
    if "back" in n:
        if len(d) > 0:
            print(d[-1])
        else:
            print(-1)
        
    

for i in range(n):
    sol(sys.stdin.readline().strip())