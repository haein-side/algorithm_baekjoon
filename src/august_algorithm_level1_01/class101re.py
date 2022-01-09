# def solution(A, B): 
#     A.sort() 
#     B.sort()

#     i = 0
#     for a in A:
#         if i < len(B) - 1 and B[i] < a:
#             i += 1

#         if a == B[i]:
#             return a
#     return -1

# print(solution([1,2,3,6], [4,5,6]))

def solution(A, B): 
    A.sort()
    B.sort()
    
    j = 0
    for i in range(len(A)):
        if A[i] < B[j] :
            i += 1
        else :
            while True :
                if A[i] > B[j] :
                    j += 1
                if A[i] == B[j] :
                    break
                if A[i] < B[j] :
                    break    
            if A[i] == B[j] :
                return A[i]
            if A[i] < B[j] :
                return -1
                    
        
# print(solution([1,2,3,6], [4,5,6]))
# print(solution([1,2,4], [2,5]))
# print(solution([1, 3, 2, 1], [4, 2, 5, 3, 2]))