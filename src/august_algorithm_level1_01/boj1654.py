# from typing import Sequence 

# K, N = map(int,input().split())

# n = []

# for i in range(K) :
#     n.append(int(input()))

# def sol(n: Sequence) -> int:
#     left = 1
#     right = max(n)
    
#     while left <= right :
#         mid = (left + right)//2
#         count = 0
#         for i in range(K):
#             count += n[i] // mid
#         if count == N :
#             print(mid)
#             break
#         if count < N : left = mid + 1
#         if count > N : right = mid - 1

# print(sol(n))


# from typing import Sequence 

# K, N = map(int,input().split())

# n = []

# for i in range(K) :
#     n.append(int(input()))

# def sol(n: Sequence) -> int:
#     left = 1
#     right = max(n)
#     answer = []
#     while left <= right:
#         mid = (left + right)//2
#         count = 0
#         for i in range(K):
#             count += n[i] // mid
#         if count == N :
#             answer.append(mid)
#         if count < N : right = mid - 1
#         if count > N : left = mid + 1
        
#     return answer

# print(sol(n))

# 왜 안되는지 모르겠는 나의 코드..

# from typing import Sequence 
# K, N = map(int,input().split())

# n = []

# for i in range(K) :
#     n.append(int(input()))

# def sol(n: Sequence) -> int:
#     left = 1
#     right = max(n)
  
#     while left <= right:
#         mid = (left + right)//2
#         count = 0
#         for i in range(K):
#             count += n[i] // mid
#         if count == N :
#             return mid
#         if count < N : right = mid - 1
#         if count > N : left = mid + 1
     
# print(sol(n))

# 다른 분 코드 참고해서 만든 풀이

from typing import Sequence 

K, N = map(int,input().split())

n = []

for i in range(K) :
    n.append(int(input()))

def sol(n: Sequence) -> int:
    left = 1
    right = max(n)
    answer = []
    while left <= right:
        mid = (left + right)//2
        count = 0
        for i in range(K):
            count += n[i] // mid
        if count < N : right = mid - 1
        if count >= N : 
          left = mid + 1 
        print("과정중",right, "N값",N,"left값",left,"right",right )
      
    return right

print(sol(n))