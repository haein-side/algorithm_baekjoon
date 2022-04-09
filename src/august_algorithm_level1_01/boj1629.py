# import sys
 
# a, b, c = map(int, sys.stdin.readline().split())

# answer = a
# for i in range(b-1):
#     answer = a * answer

# print(answer%c)

import sys
 
a, b, c = map(int, sys.stdin.readline().split())

cnt = 0
def sol(n):
    global cnt
    
    # if cnt == b:
    #     return 1
    if cnt < b:
        cnt += 1
        return n * sol(n)
    else:
        return 1
    # return

answer = sol(a)
print(answer%c)