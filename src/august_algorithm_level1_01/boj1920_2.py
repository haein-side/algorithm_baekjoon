import sys
m = int(sys.stdin.readline())
mlist = sorted(list(map(int, sys.stdin.readline().split()))) # 이 리스트 중에 타겟이 있는지 찾는 것
n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split())) # 타겟이 들어가 있는 리스트

def bsearch(start, end, mid, target):

    if start > end:
        return 0

    mid = (start + end) // 2
    
    if target == mlist[mid]:
        return 1
    if target < mlist[mid]:
        end = mid -1
    if target > mlist[mid]:
        start = mid + 1
        
    return bsearch(start, end, mid, target) # 여기서 왜 return을 써줘야 하는지 잘 모르겠음

for i in nlist:
    print(bsearch(0, len(mlist)-1, (len(mlist)-1)//2, i))