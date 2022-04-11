import sys

n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()

alist = [] # 순서대로 되어 있는 리스트
answer = []

for i in range(len(num)):
    alist.append(int(num[i]))

stack = []
cnt = 0
tmp = 0
for i in range(n):
    while stack:
        if cnt == k-1:
            tmp = i
            break
            # answer.append(alist[i])
        if stack[-1] <= alist[i]:
            stack.pop()
            answer.append(alist[i])
            stack.append(alist[i])
        else:
            stack.append(alist[i])
            cnt += 1
    
    stack.append(alist[i])

if tmp != 0 and tmp < n-1:
    answer.append(alist[i+1:n])

print(answer)