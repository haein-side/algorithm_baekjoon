import sys
input = sys.stdin.readline
cnt = 0
n, r, c = map(int, input().split())

def sol(k, row, col): # 현재 한 변의 길이 k, 현재 행의 위치 row, 현재 열의 위치 col
    global cnt
    # 목표 위치에 도달했을 때
    if row == r and col == c:
        print(cnt)
        exit(0)
        # 이렇게 코드를 짜면 안되는 이유 : 나머지 재귀가 또 새로 돌아가기 때문에 
        # global 함수를 써서 바로 출력 후 종료해줘야 함

    # 현재 범위 안에는 있는데 하나씩 쪼개서 값을 더해줘야 할 때
    if k == 1:
        cnt += 1
        return
    
    # 현재 범위 안에 값이 없을 때
    if not (row <= r <= row+k-1 and col <= c <= col+k-1): 
        cnt += k*k
        return

    sol(k//2, row, col)
    sol(k//2, row, col + k//2)
    sol(k//2, row + k//2, col)
    sol(k//2, row + k//2, col + k//2)

sol(2**n, 0, 0)

