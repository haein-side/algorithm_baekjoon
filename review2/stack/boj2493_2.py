# 2493번 탑
import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    tap = list(map(int, input().split()))

    answer = [0 for _ in range(n)] # 답안이 들어가는 리스트
    stack = [] # 레이저를 수신받은 탑의 위치(인덱스)

    for i in range(n):
        while stack and tap[stack[-1]] < tap[i]:
            stack.pop()
        
        if stack: # while문 마치고도 스택에 남아있으면 -> tap[i]보다 큰 값
            answer[i] = stack[-1] + 1
        
        stack.append(i) # 현재 탑의 index를 stack에 저장해줘야 함

    for i in answer:
        print(i, end = " ")

sol()


