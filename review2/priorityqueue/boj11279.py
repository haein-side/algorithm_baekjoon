from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
numlist = deque()

for i in range(n):
    num = int(input())
    numlist = sorted(numlist)
    if num == 0:
        if len(numlist) > 0:
            print(numlist.pop())
        else:
            print(0)
    else:
        numlist.append(num)
