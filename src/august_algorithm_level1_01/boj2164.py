import sys
from collections import deque

N = int(sys.stdin.readline())

numlist = []

for i in range(N):
    numlist.append(i+1)
    
deq = deque(numlist)

if N == 1:
    print(numlist[0])
elif N == 2:
    print(numlist[1])
else:
    for i in range(N-2):
        deq.popleft()
        num = deq.popleft()
        deq.append(num)
    print(deq[1])