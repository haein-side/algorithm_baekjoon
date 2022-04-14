import sys

N = int(sys.stdin.readline())
W = []
stack = []

for i in range(N):
    W.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    l = W[i][0] - W[i][1]
    r = W[i][0] + W[i][1]
    stack.append(l)
    stack.append(r)

t = []

for i in range(len(stack)):
    if i % 2 == 0:
        t.append([stack[i], 1]) # 여는 거 (좌표와, 1 // -1)
    else:
        t.append([stack[i], -1]) # 닫는 거

t = sorted(t, key = lambda x : (x[0], x[1])) # 닫는 걸 먼저 나오게 정렬

res = 0
mstack = []
for i in range(len(t)):
    if t[i][1] == 1: # 여는 거
        mstack.append(t[i])
    elif t[i][1] == -1: # 닫는 거 
        if mstack[-1][1] == 1:
            res += 1
            a = mstack.pop()
            mstack.append([t[i][0]-a[0], 3]) # [지름, 원(3)]
        elif mstack[-1][1] == 3:
            circle = 0
            while True:
                M = mstack.pop()
                if M[1] == 3:
                    circle += M[0]
                if M[1] == 1: # 여는 부분이 나올 때까지 pop을 해야 함
                    tmpc = t[i][0] - M[0]
                    break
            # print('circle', circle, 'tmpc', tmpc)
            if tmpc == circle:
                res += 2
                mstack.append([t[i][0]-M[0], 3])
            else:
                res += 1
                mstack.append([t[i][0]-M[0], 3])    
            

print(res+1)
            
    