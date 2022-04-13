import sys
N, K = map(int, sys.stdin.readline().split())
tmp = sys.stdin.readline()
num = []
for i in range(N):
    num.append(int(tmp[i]))

stack = []
cnt = K
for i in range(len(num)):
    # cnt가 0보다 크다는 조건으로 cnt가 0이 되었을 때 더이상 팝하지 못하게 했음
    # pop 횟수 초과 시 자동으로 밑에서 stack에 append만 됨!!
    while stack and cnt > 0:
        if stack[-1] >= num[i]:
            break
        else:
            stack.pop()
            cnt -= 1
    # stack에 append는 모든 원소를 넣는 것
    stack.append(num[i])
    
for i in range(N-K):
    print(stack[i], end = "")
    
    
    