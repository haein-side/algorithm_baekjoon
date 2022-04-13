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
        return arr[-2]
        
    lt = dconquer(n//2, x, y)
    lb = dconquer(n//2, x, y + n//2)
    rt = dconquer(n//2, x + n//2, y)
    rb = dconquer(n//2, x + n//2, y + n//2)
    arr2 = [lt, lb, rt, rb]
    arr2.sort()
    return arr2[-2]

print(dconquer(N, 0, 0))