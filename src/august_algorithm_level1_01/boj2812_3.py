import sys

n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()

alist = [] # 순서대로 되어 있는 리스트
answer = []

for i in range(len(num)):
    alist.append(int(num[i]))

stack = []
cnt = 0
for i in range(n):
    while stack:
        if cnt == k:
            break
        if stack[-1] < alist[i]:
            answer.append(alist[i])
            stack.pop()
            cnt += 1
        elif stack[-1] > alist[i]:
            stack.append(alist[i])
            cnt += 1
        else:
            stack.append(alist[i])
        
    stack.append(alist[i])

print(answer)