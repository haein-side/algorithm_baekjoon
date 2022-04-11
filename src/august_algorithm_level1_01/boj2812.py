import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
number = sys.stdin.readline()
stack = [] # 전체 숫자

for i in range(N):
    stack.append(int(number[i]))

result = []
cur = [] # 현재 뽑은 숫자

def splice(stack, i):
    return stack[0:i] + stack[i+1:len(stack)]

def sol(stack, c): # stack 중에서 c개를 선택해야 한다는 뜻
    global cur, result
    curlen = len(stack)
    
    if c <= 0: # 더이상 선택할 c가 남아있지 않다는 뜻
        print(cur)
        result.append(cur)
        return
    
    for i in range(curlen):
        cur.append(stack[i])
        sol(splice(stack,i), c-1)
        cur.pop()

sol(stack, K)
print(result)