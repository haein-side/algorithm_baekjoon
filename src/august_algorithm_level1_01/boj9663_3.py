import sys

n = int(sys.stdin.readline())
mlist = [0]*n # n개의 행을 할당한 1차원 리스트
# visited = [False]*n # 방문 안 했으면 False, 방문 했으면 True

def check(mlist, row) :
    # 열은 재귀에서 계속 하나씩 더해지니까 같을 수가 없음
    # 대각선 조건도 생각해야
    for i in range(row):
        # row를 기준으로 도는 이유 : row 미만의 행들만 제대로 놓여져 있기 때문! search(mlist, row+1)
        # 다른 열들 중 행이 같은 게 있거나 대각선 상에 있는 것들은 제외!  
        if mlist[row] == mlist[i] or abs(mlist[i]-mlist[row]) == row - i: # row개만큼 돌리기 때문에 i는 row보다 작음 -> row - i를 해야 양수의 차이를 얻을 수 있음!!!
            return False # 방문할 수 없으면 False
    return True # 방문할 수 있으면 True

def search(mlist, row): # 컬럼은 필요가 없고 for문으로만 사용하는 것!
    n = len(mlist)
    result = 0
    if row == n:
        # result += 1
        # return result
        return 1 # 한 번 다 놓으면 1을 리턴해줌
    
    for col in range(n):
        mlist[row] = col # 이렇게 둬도 어차피 같은 행에서 반복문 돌면서 col 갱신되므로 괜찮음!
        if check(mlist, row): # check() 함수에서 False가 나오면 재귀함수를 실행하지 않고 다음 열로 반복문을 돎
            # visited[row] = True
            result += search(mlist, row+1)
            # visited[row] = False
            
    return result
    
    

print(search(mlist, 0))
