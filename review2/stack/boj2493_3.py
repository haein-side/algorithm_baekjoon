# 현진 언니 풀이
from sys import stdin 
input = stdin.readline

# n 범위 10억, 1.5초 -> for문 1회

def main():

    n = int(input())
    tops = list(map(int, input().split()))

    stack = []      # 레이저를 수신할 탑의 위치를 저장(현재 탑보다 height가 큰 것)
    receive = [0]*n # 레이저를 수신받은 탑의 위치(현재 탑보다 근접한 높은탑)

    for i in range(n):
        while stack and tops[stack[-1]] <= tops[i]:     # 테스트케이스 추가된듯?! 등호 <=  
            stack.pop()                                 

        if stack:                       # while문을 마치고도 스택이 있으면 = i보다 큰탑
            receive[i] = stack[-1] + 1  # i위치에 수신받은 위치값 저장(0부터 시작한 index이므로 +1)
        
        stack.append(i)  
    
    print(" ".join(map(str, receive)))  
    # print(" ".join(receive))    # int형의 list는 join이 안됨
    # print(*receive)   # 속도 2배 걸림

main()