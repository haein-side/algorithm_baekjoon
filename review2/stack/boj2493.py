# 2493번 탑
import sys
input = sys.stdin.readline

n = int(input())
tap = list(map(int, input().split()))
dic = {}
for i in range(n):
    dic[tap[i]] = i+1

answer = [0] # 답안이 들어가는 리스트
stack = [tap[0]] # 기준이 될만한 것들만 남겨두는 stack

for i in range(1, n):
    flag = False
    for j in range(len(stack)):
        if tap[i] < stack[-1]:
            answer.append(dic.get(stack[-1]))
            flag = True
            break
        elif tap[i] > stack[-1]:
            stack.pop()
    stack.append(tap[i])
    if not flag : # 하나의 탑도 맞추지 못한 경우
        answer.append(0)

for i in answer:
    print(answer[i], end = " ")
            


