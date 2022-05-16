import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
num = deque(i for i in range(1, n+1))

j = 1
while (len(num) > 1):
    if j % 2 == 1:
        num.popleft()

    else:
        num.append(num[0])
        num.popleft()
    j += 1

print(num[0])