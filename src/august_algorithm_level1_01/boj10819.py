import itertools
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr)
a = 0 # 전그룹 중 최대값
i = 0 # 전그룹 중 최대값의 인덱스
if n % 2 == 0:
    a = arr[len(arr)//2-1]
    i = len(arr)//2-1
else:
    a = arr[(len(arr)-1)//2]
    i = (len(arr)-1)//2

alist = arr[0:i+1]
blist = sorted(arr[i+1:], reverse = True)

answer = [None]*n
answer[0] = alist[len(alist)-1]

for i in range(len(alist)-1):
    answer[(i+1)*2] = alist[i]
    
for i in range(len(blist)):
    answer[(i+1)*2-1] = blist[i]
print(answer)
sum = 0
for i in range(0, len(answer)-1):
    sum += abs(answer[i]-answer[i+1])

print(sum)