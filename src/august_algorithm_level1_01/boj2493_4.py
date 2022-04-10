import sys

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
answer = [0 for _ in range(N)] # 아무 액션도 일어나지 않았을 때 이미 0으로 초기화되어 있음
stack = []

for i in range(N): # 탑의 원소별 반복문
    while stack: # 스택에 값이 존재할 때
        if stack[-1][1] > top[i]: # 스택에 들어간 마지막 값 > 현재 탑의 높이 (수신가능)
            answer[i] = stack[-1][0]+1 
            break
        else: # 스택에 들어간 마지막 값 < 현재 탑의 높이 (수신불가)
            stack.pop()
    
    stack.append([i, top[i]]) # 스택에 값이 존재하지 않을 때 이차원 배열로 스택에 인덱스 값과 원소값을 넣어줌

print(*answer)