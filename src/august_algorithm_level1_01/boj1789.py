import sys

S = int(sys.stdin.readline())

m = 0
while m <= S:
    if m * (m + 1) == 2 * S:
        print(m)
        break
    elif m * (m + 1) > 2 * S:
        print(m-1)
        break
    m += 1
# print(m-1)
# def bsearch():
#     start = 1
#     end = m
#     while start <= end:
#         mid = (start + end) // 2
#         sum = mid * (mid + 1) // 2
#         left = S - sum
#         if left == 0:
#             return mid
#         if left > mid :
#             start += 1
#         elif left < mid :
#             return mid
#     return None    
    
# print(bsearch())