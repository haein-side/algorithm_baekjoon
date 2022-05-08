# N-Queen
# 대각선 조건 고려 O
import sys
input = sys.stdin.readline

n = int(input())
# pos[열] = 행
# pos[col] = row
pos = [0 for _ in range(n)] # 각 열의 어느 행에 뒀는지 확인

def check(col): 
    # 지금까지 놓은 열 중 같은 행에 둔 게 있는지 확인
    # 열이 인덱스의 역할을 함
    for i in range(col):
        if pos[col] == pos[i] or abs(pos[col]-pos[i]) == col - i: # col은 i보다 큼 (양수)
            return False
    return True

def place(col):
    count = 0
    if col == n: # 열의 끝까지 뒀으면
        return 1 # 1개의 경우의 수 반환
    
    for row in range(n): # 하나의 열(col)에 대해 for문을 돌며 놓을 수 있는 행(row)에 놓아봄
        pos[col] = row # 열(col) 행(row)에 위치시킴
        if check(col): # 아직 안 놓은 행이면
            count += place(col+1)
    
    return count

# 0열부터 시작
print(place(0)) # 대각선 조건 고려하지 않을 때는 40320이 출력됨
