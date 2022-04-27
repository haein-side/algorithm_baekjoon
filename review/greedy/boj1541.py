import sys
input = sys.stdin.readline

n = input().rstrip()
m = n.split('-')
tmp = []
for i in m:
    tmp.append(sum(map(int, i.split('+'))))
res = 0
for i in range(len(tmp)):
    if i == 0:
        res += tmp[i]
    else:
        res -= tmp[i]

print(res)