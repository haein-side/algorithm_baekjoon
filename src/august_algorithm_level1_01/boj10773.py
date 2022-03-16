from re import L
import sys
from collections import deque

k = int(sys.stdin.readline())
dq = deque([])

for i in range(k):
    dq.append(int(sys.stdin.readline()))

while 0 in dq:
    a = dq.index(0)
    b = a - 1
    
    dq.remove(a)
    dq.remove(b)


print(sum(dq))