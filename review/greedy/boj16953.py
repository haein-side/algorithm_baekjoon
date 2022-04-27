import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
queue = deque([(a, 1)]) # 큐에 (현재 숫자, 연산 횟수) append
res = -1

while queue:
    until, cnt = queue.popleft()
    
    # 숫자가 목표 숫자와 동일해지면 while문 끝내기
    # 큐에 들어간 숫자 중에 지금까지의 연산 결과가 b와 같아지면 "바로" break함! == "최소" 연산이라고 말할 수 있는 이유!
    if until == b:
        res = cnt
        break
    
    # 2를 곱했을 때 b보다 크면 큐에 넣지 않음 => 이하이면 큐에 넣음
    if until * 2 <= b:
        queue.append((until*2, cnt+1))
    
    # 오른쪽에 1을 더했을 때 b보다 크면 큐에 넣지 않음 => 이하이면 큐에 넣음
    if int(str(until) + "1") <= b:
        queue.append((int(str(until) + "1"), cnt+1))

print(res)