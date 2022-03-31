import sys
nlist = []
n, a = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
alist = []
for i in nlist:
    if i < a:
        alist.append(i)
        
answer = ''

for i in alist:
    answer = answer + str(i) + ' '

print(answer.strip())