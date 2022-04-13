# 탑
import sys

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []
for i in range(len(top)):
    while stack: # 비교할 대상이 앞에 있을 때
        if stack[-1][1] > top[i]:
            answer.append(stack[-1][0] + 1) # 해당 스택의 인덱스 + 1
            break # 수신할 탑을 정해줬으므로 더이상 while문을 돌 필요가 없음!! (break 해주기)
        else:
            stack.pop()
    if not stack: # 비교할 대상이 앞에 없으므로 0
        answer.append(0)
    stack.append([i, top[i]])

print(*answer)