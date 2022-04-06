import sys

n, r, c = map(int,sys.stdin.readline().split())
result = 0
def sol(k, row, col): # k: 한 변의길이 row: 현재 행의 위치 col: 현재 열의 위치
    global result
    
    if row == r and col == c:
        print(result)
        exit(0)
    
    if k == 1:
        result += 1
        return
    
    if not(row <= r <= row+k-1 and col <= c <= col+k-1): # 해당 사분면에 원하는 좌표가 없을 경우
        result += k*k # 한 변의 길이 k를 제곱해서 들어 있는 모든 박스의 개수를 다 넣어줌
        return
    
    # 제 1사분면
    sol(k//2, row, col)
    
    # 제 2사분면
    sol(k//2, row, col + k//2)
    
    # 제 3사분면
    sol(k//2, row + k//2, col)
    
    # 제 4사분면
    sol(k//2, row + k//2, col + k//2)
    

sol(2**n, 0, 0)