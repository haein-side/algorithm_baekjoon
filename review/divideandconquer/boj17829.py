import sys

N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

def dconquer(n, x, y) : # n : 현재 변의 길이, x : 현재 좌표의 행 위치, y : 현재 좌표의 열 위치
    
    if n == 2: # 한 변의 길이가 2일 때
        arr = []
        arr.append(A[x][y])
        arr.append(A[x][y+1])
        arr.append(A[x+1][y])
        arr.append(A[x+1][y+1])
        arr.sort()
        a = arr[2]
        # for i in range(len(arr)):
        #     if arr[i] != a:
        #         del A[]
    dconquer(n//2, x, y)
    dconquer(n//2, x, y + n//2)
    dconquer(n//2, x + n//2, y)
    dconquer(n//2, x + n//2, y + n//2)

dconquer(N, 0, 0)