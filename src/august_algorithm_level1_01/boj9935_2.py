import sys

w = list(sys.stdin.readline().strip()) # 스택
t = list(sys.stdin.readline().strip())
stack = []

for i in range(len(w)):
    stack.append(w[i])
    if stack and w[i] == t[-1]: # 타겟의 마지막 값과 w 리스트의 현재 값이 같으면
        if stack[-len(t):] == t:
            for j in range(len(t)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))
