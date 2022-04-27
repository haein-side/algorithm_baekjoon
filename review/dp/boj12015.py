# 가장 긴 증가하는 부분 수열 2

# 풀이 1 - 시간초과 남
# import sys
# input = sys.stdin.readline

# n = int(input())
# num = [0] + list(map(int, input().split()))
# dp = [1 for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1, i): # 인덱스 0인 것부터 비교하면 초기화가 1로 되어 있어 수가 하나 더 더해지게 됨
#         if num[i] > num[j]:
#             dp[i] = max(dp[i], dp[j]+1)
            
# print(max(dp))

# 풀이 2 - 이분탐색을 이용한 풀이
# import sys
# input = sys.stdin.readline

# n = int(input())
# num = list(map(int, input().split()))
# res = [num[0]]

# def find(target):
#     start = 0
#     end = len(res)-1
#     while start <= end:
#         mid = (start + end) // 2
        
#         if res[mid] == target:
#             return mid
#         elif res[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
        
#     return start # 일치하는 값이 없어 더이상 이진탐색을 할 수 없을 때 end를 리턴

# for item in num:
#     if res[-1] < item: # 부분 수열에 들어있는 마지막 원소보다 num[i]가 크면 수열에 바로 넣을 수 있음
#         res.append(item)
#     else:
#         res[find(item)] = item
        
# print(len(res))

import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
res = [0]

def find(target):
    start = 1
    end = len(res)
    while start <= end:
        mid = (start + end) // 2
        
        if res[mid] == target:
            return mid
        elif res[mid] < target:
            start = mid + 1
        elif res[mid] > target:
            end = mid - 1  
    return start # 일치하는 값이 없어 더이상 이진탐색을 할 수 없을 때 start를 리턴 (왜 end가 안되는지 모르겠음..)

for i in range(1, n+1):
    if res[-1] < num[i]: # 부분 수열에 들어있는 마지막 원소보다 num[i]가 크면 수열에 바로 넣을 수 있음
        res.append(num[i])
else:
        idx = find(num[i])
        res[idx] = num[i]

print(len(res) - 1)