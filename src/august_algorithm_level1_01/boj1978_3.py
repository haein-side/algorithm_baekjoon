import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
c = 0
a = False
for i in nlist:
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else: # loop 이후에 else만 쓰이면 for문이 모두 끝난 이후에 한 번 실행됨
        c += 1
        
print(c)