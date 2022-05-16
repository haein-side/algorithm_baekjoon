from collections import deque
import sys
input = sys.stdin.readline

stack = deque()
n = int(input())

for i in range(n):
    a = input().strip()
    flag = False
    for j in a:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif len(stack) > 0 and stack[-1] == ")":
                flag = True
                print("NO")
                break
            elif len(stack) == 0:
                flag = True
                print("NO")
                break
    if len(stack) == 0 and not flag:
        print("YES")