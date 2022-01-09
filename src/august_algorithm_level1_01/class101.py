# # 문제 1 (솔)
# def solution(s):
#     c = s[0]
#     if c.isupper():    # please fix condition
#         return "upper"
#     elif c.islower():  # please fix condition
#         return "lower"
#     elif c.isdigit():  # please fix condition
#         return "digit"
#     else:
#         return "other"

# # print(solution(input()))

# # 문제 2 (테스트 케이스 몇 개만 솔)
# def solution(A, B): 
#     # A = [3 1 4 5 7]
#     # B = [2 3 1 6]
#     A.sort() 
#     B.sort()
#     print(f"A: {A}")
#     print(f"B: {B}")
#     # A = [1 3 4 5 7]
#     # B = [1 2 3 6]
#     for a in A:
#         i = 0
#         if i < len(B) - 1 and B[i] < a:
#             i += 1
#             if a > B[i] : i +=1
#             print(f"i: {i}")
            
#         print(f" 중간 점검 : {a},{B[i]}")

#         if a == B[i]:
#             print(f"{a},{B[i]}")
#             return a
#     return -1

# print(solution([1,2,3,6], [4,5,6]))
# # print(solution([1,2,4], [2,5]))
# # print(solution([1, 3, 2, 1], [4, 2, 5, 3, 2]))

# 문 2 - 제시된 문제
def solution(A, B): 
    A.sort() 
    B.sort()

    i = 0
    for a in A:
        while i < len(B) - 1 and B[i] < a:
            i += 1

        if a == B[i]:
            return a
    return -1

print(solution([1,2,3,6], [4,5,6]))
print(solution([1,2,4], [2,5]))
print(solution([1, 3, 2, 1], [4, 2, 5, 3, 2]))
print(solution([1,2],[3,5]))