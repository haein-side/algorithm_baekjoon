import sys
input = sys.stdin.readline

n = int(input())
board = [0 for _ in range(n)] 
# board[열(col)] = 행(row) 
# 열이 인덱스 역할

def check(col): # 해당 열의 행에 둘 수 있는지 확인
    for i in range(col):
        if board[i] == board[col] or abs(board[i]-board[col]) == col - i:
            return False
    return True # return 위치 실수했었음!!!

def dfs(col): # 현재 열
    count = 0
    if col == n: # 현재 열이 끝에 도달했을 때
        return 1
    flag = False
    for row in range(n): # 하나의 col에 n개의 row를 모두 위치시켜봄
        board[col] = row # 여기서 board[col] = row로 초기화해준 값을 가지고
        if check(col):   # check(col)에서 놓을 수 있는지 확인해보는 것!
            flag = True
            count += dfs(col + 1) # 해당 행에 놓을 수 있다면 다음 열로 재귀 탐색
    
    return count
    
print(dfs(0))

'''
visited 처리 필요 없는 이유
board 배열에 값을 갱신하면서 더해주거나 빼주는 구조가 아니라, 
재귀가 한 번 돌 때마다 board[col] = row 로 값을 새롭게 대입해주는 방식이기 때문

또한 구해야 하는 값인 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수는 
변수 count 에 계속 쌓이고 있음
'''