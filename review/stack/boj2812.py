# 크게 만들기
import sys

N, K = map(int, sys.stdin.readline().split())
tmp = sys.stdin.readline()
num = []
stack = []
for i in range(N):
    num.append(int(tmp[i]))

cnt = K
for i in range(N):
    while stack and cnt > 0:
        if stack[-1] < num[i]:
            stack.pop() # 더이상 stack이 기준 역할을 제대로 못하므로 pop
            cnt -= 1
        else: # stack에 있는 값이 나보다 크면 그대로 두고 break (스택이 기준 역할을 하고 있으므로)
            break
    
    stack.append(num[i])

for i in range(N-K):
    print(stack[i], end="")