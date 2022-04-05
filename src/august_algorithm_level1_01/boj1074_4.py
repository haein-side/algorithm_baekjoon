import sys

n, r, c = map(int, sys.stdin.readline().split())

result = 0

def sol(n, x, y): # n: 현재 변의 길이, x: 현재 좌표의 행의 위치, y: 현재 좌표의 열의 위치
    global result
    if x == r and y == c:
        print(result) 
        # 여기에 만약 return result라면 값이 함수로 돌아오기만 하지 sol함수 자체가 끝나는 것이 아님!!
        # 다음 라인의 exit(0)이 실행되지도 못하고 다시 함수쪽으로 돌아가서 다음 함수가 실행됨!!
        # 그 아래에 재귀함수가 계속 실행됨 (계속 result에 값이 더해짐 but 그러면 안되는 것!)
        exit(0)
    
    if n == 1:
        result += 1
        return # 재귀 호출해준 곳 다음으로 내려감 -> 그래야 더 n을 나누지 않고 다음 사분면으로 좌표를 옮길 수 있음
    
    if not (x <= r <= x+(n-1) and y <= c <= y+(n-1)): # x축에 목표가 없거나 y축에 목표가 없을 때 (드모르간 법칙)
        result += n*n
        # print(n, result)
        return # 더이상 그 함수 볼 필요 없으므로 바로 return 해줌
    
    sol(n//2, x, y) # 제 1사분면
    sol(n//2, x, y + n//2) # 제 2사분면 // n이 2인 경우 1만 더해져서 2*2인 사각형에서 좌표를 하나씩 옮길 수 있음
    sol(n//2, x + n//2, y) # 제 3사분면
    sol(n//2, x + n//2, y + n//2) # 제 4사분면
    
sol(2**n, 0, 0) # (0,0)부터 시작