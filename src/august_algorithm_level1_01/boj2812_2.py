# 처음 풀이 (마지막 예제 충족 X)
import sys

n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()

alist = [] # 원래 수의 순서대로 되어 있는 리스트

for i in range(len(num)):
    alist.append(int(num[i]))

nlist = sorted(alist, reverse = True) # 역순 리스트

tmp = [] # pop()하는 수를 저장해두는 리스트
for i in range(k):
    a = nlist.pop()
    tmp.append(a)

for i in range(len(tmp)):
    alist.remove(tmp[i])

print(*alist)