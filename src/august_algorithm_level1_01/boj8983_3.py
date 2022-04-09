# import sys
# input = sys.stdin.readline

# m, n, l = map(int, input().split())
# shootpos = list(map(int, input().split()))
# shootpos.sort()

# # 동물을 기준으로 자신을 죽일 수 있는 사대가 있는지를 이분 탐색했다.
# # 있을 경우 count가 올라간다.

# count = 0
# for _ in range(n):
#     x, y = map(int, input().split())

#     left = 0
#     right = len(shootpos)-1
#     # print(x, y)

#     # 이분 탐색
#     if l >= y:

#         while left <= right:
#             inix = 0
#             mid = (left + right) // 2
#             inix = shootpos[mid]
            
#             if (y <= l and inix-l <= x <= inix + l) and (x - (inix-l) >= y and x - inix + y <= l):
#                 # x, y가 뾰족한 이등변 삼각형 안에 잘 들어와있는지 체크. 기본적으로 0,0좌표로 옮기고 eg(-inix) 조건을 줬다.

# 				count += 1
#                 # break

#             if x >= inix:
#                 left = mid + 1

#             else:
#                 right = mid - 1


# print(count)