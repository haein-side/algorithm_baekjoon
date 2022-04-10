import sys

N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

res = ['0']
for i in range(1, N):
    stack = s[0:i][::-1] # 해당 원소 전까지 그리고 역순을 취해줌 
    j = 0
    while j < len(stack):
        if s[i] > stack[j]:
            stack.pop()
        else:
            res.append(str(s.index(stack[j]) + 1))
            break
        j += 1
    if len(stack) == 0:
        res.append(str(0))
        
print(" ".join(res))