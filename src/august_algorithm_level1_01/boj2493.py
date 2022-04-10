import sys
import collections
N = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(N-1, -1, -1):
    stack = collections.deque(t[0:i])
    count = 0
    n = len(stack)-1 # 스택의 마지막 인덱스
    while n >= 0:
        if stack[n] < t[i]:
            stack.pop()
        else:
            count += 1
            result.append(str(n+1))
            break
        n -= 1
    if count == 0:
        result.append(str(0))

print(" ".join(result[::-1]))
    