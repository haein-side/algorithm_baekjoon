import sys

n, r, c = map(int, sys.stdin.readline().split())
arr = [[0,0]] * 2**n  # 2의 n승 개의 박스
print(arr)

def sol(n, r, c, arr):
    if r == 2**n-1 and c == 2**n-1:
        return 1
    
    for i in range(4):
        arr









print(sol(n, r, c))
