import sys

n, r, c = map(int,sys.stdin.readline().split())
result = 0
def sol(k, row, col): # k: 한 변의길이 row: 현재 행의 위치 col: 현재 열의 위치
    global result
    
    '''
    놓친 것 1.
    재귀함수는 종료조건을 만날 때까지 계속 돌음!
    언제까지 계속 돌아야 하는지 케이스를 잘 나눠야
    1) 현재 행과 열의 위치가 목표 지점에 도달한 경우
    2) 해당 사분면 안에 아예 원하는 좌표가 없는 경우
    3) 해당 사분면 안에는 있는데 원하는 좌표는 아닌 경우 
       끝까지 나눠서 k==1일 때까지 나누고 result에 하나씩 더해줘야

    놓친 것 2. 
    global 변수의 사용
    '''
    if row == r and col == c: # 현재 행의 위치 == 목표 행 이고 현재 열의 위치 == 목표 열일 때
        print(result)
        exit(0)
    
    if k == 1: # 해당 사분면 안에는 있는데 원하는 좌표는 아닌 경우에 result += 1
        result += 1
        return
    
    if not(row <= r <= row+k-1 and col <= c <= col+k-1): # 해당 사분면에 원하는 좌표가 없을 경우
        result += k*k # 한 변의 길이 k를 제곱해서 들어 있는 모든 박스의 개수를 다 넣어줌
        return
    
    # 제 1사분면
    sol(k//2, row, col)
    # 제 2사분면
    sol(k//2, row, col + k//2) # 행은 그대로인데 열이 k//2만큼 더해짐
    # 제 3사분면
    sol(k//2, row + k//2, col) # 열은 그대로인데 행이 k//2만큼 더해짐
    # 제 4사분면
    sol(k//2, row + k//2, col + k//2) # 행과 열이 모두 k//2만큼 더해짐
    
sol(2**n, 0, 0)