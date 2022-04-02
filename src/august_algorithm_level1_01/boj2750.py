import sys

n = int(sys.stdin.readline())
nlist= []
for i in range(n):
    nlist.append(int(sys.stdin.readline()))

nlist = sorted(nlist)

for i in nlist:
    print(i)