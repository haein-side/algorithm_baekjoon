import sys

N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
s = s[::-1] # 스택을 역순으로

res = []
for i in range(N):
    count = 0
    for j in range(i+1, N):
        if s[i] > s[j]:
            continue
        elif s[i]< s[j]:
            res.append(str(N-j))
            count = 1
            break
    if count == 0:
        res.append(str(0))

print(" ".join(res[::-1]))


