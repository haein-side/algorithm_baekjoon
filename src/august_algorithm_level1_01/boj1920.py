from typing import Sequence

N = int(input())
A = list(map(int,input().split()))

A.sort()

M = int(input())
B = list(map(int,input().split()))

# 시간초과
# for i in range(len(A)) :
#     if B[i] in A : print("1") 
#     else : print("0")

def bin_search(A:Sequence, target:int) -> bool :
    pl = 0
    pr = N - 1
    
    while pl <= pr:
        pc = (pl + pr) // 2
        if A[pc] == target :
            return True
        
        if A[pc] < target :
            pl = pc + 1
        elif A[pc] > target :
            pr = pc - 1

for i in range(M) :
    if bin_search(A, B[i]) :
        print("1")
    else :
        print("0")
