# 시간초과
# for i in range(len(A)) :
#     if B[i] in A : print("1") 
#     else : print("0")

from typing import Sequence

N = int(input())
A = list(map(int,input().split()))

A.sort()

M = int(input())
B = list(map(int,input().split()))

def bin_search(A:Sequence, target:int) -> bool :
    left = 0
    right = N - 1
    
    while left <= right:
        pc = (left + right) // 2
        if A[pc] == target :
            return True
        elif A[pc] < target :
            left = pc + 1
        else :
            right = pc - 1

for i in range(M) :
    if bin_search(A, B[i]) :
        print("1")
    else :
        print("0")
