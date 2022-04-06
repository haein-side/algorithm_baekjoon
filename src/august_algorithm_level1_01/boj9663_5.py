import sys

# 이번에는 열을 기준으로 N-Queen 문제 풀어보기
n = int(sys.stdin.readline())
count = 0
arr = [0 for i in range(n)] # ex. arr[0] = 4 라고 하면 0열 4행에 퀸이 있는 것

def check(col):
    for i in range(col): # 처음에 n으로 뒀었음
        # if col != i: # col 자기 자신을 제외하고 비교해준다고 생각했으나, 재귀 때문에 열이 하나씩 더해지기 때문에 for i in range(row)로 둬야!
            if arr[col] == arr[i] or abs(arr[col]-arr[i]) == col - i: # i가 col 미만까지 돌기 때문에 col - i는 양수일 수밖에 없음!
                return False # 방문할 수 없으면 False 반환
    return True # 방문할 수 있으면 True 반환
            

def queen(col):
    global n, count, arr
    
    if col == n:
        count += 1
        return
    
    for i in range(n):
        arr[col] = i
        if check(col):
            queen(col+1)
            arr[col] = 0 # 재귀 끝난 후, arr[col]을 0으로 리셋해줌


queen(0)
print(count)
