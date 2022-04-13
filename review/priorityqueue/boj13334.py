import sys

n = int(sys.stdin.readline())
p = []
for i in range(n):
    p.append(sorted(list(map(int, sys.stdin.readline().split()))))
p = sorted(p, key = lambda x : x[1])
d = int(sys.stdin.readline())
answer = []

for i in range(len(p)):
    s = p[i][0]
    e = p[i][1]
    lim = e - d
    cnt = 0
    for j in range(i+1):
        if lim <= p[j][0]:
            cnt += 1
    answer.append(cnt)

print(max(answer))
