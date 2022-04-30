import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())

queue = deque()
queue.append((a, 1))

while queue:
    num, cnt = queue.popleft()
    
    if num == b:
        print(cnt)
        break
    
    if 2 * num <= b:
        queue.append((num*2, cnt+1))
    if int(str(num) + "1") <= b:
        queue.append((int(str(num) + "1"), cnt+1))
    