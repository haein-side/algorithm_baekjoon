# import sys
# from itertools import combinations_with_replacement

# def sosu():
#     nlist = [] # 각각의 수 이하의 소수 모음
    
#     for i in range(2, 10001):
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 break
#         else:
#             nlist.append(i)
#     return nlist

# def sol(n, nlist):
#     mlist = [] # nlist 중복허용 조합
#     mlist = list(combinations_with_replacement(nlist, 2))
    
#     alist = [] # 소수의 합이 n이 되는 것
#     for i in range(len(mlist)):
#             if mlist[i][0] + mlist[i][1] == n:
#                 alist.append([mlist[i][0], mlist[i][1], (mlist[i][1] - mlist[i][0])])
    
#     alist = sorted(alist, key = lambda x: x[2])
    
#     a1 = alist[0][0]
#     a2 = alist[0][1]
#     answer = str(a1) + " " + str(a2)
#     return print(answer)


# t = int(sys.stdin.readline())

# nlist = sosu()

# for i in range(t):
#     n = int(sys.stdin.readline())
#     sol(n, nlist)