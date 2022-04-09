import sys

m, n, L = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
d = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    d[i] = list(map(int, sys.stdin.readline().split())) # 동물을 그냥 1차원 리스트로 받음

s = sorted(s) # 동물을 기준으로 잡을 수 있는 사대가 몇 개인지 확인 (사대가 정렬되어 있어야)

# 사대라는 검색대상에서 범위로 된 동물 타겟 값을 찾아줘야 하는 것

count = 0
def bsearch(d): # 동물을 하나씩 넣어줌
    x = d[0]
    y = d[1]
    s = x + y - L
    e = x - y + L
    global count
    
    # 검색대상 : 사대
    start = 0
    end = len(s)-1
    
    if y <= L :
        while start <= end:
            mid = (start + end) // 2
            
            if s[mid] >= s and s[mid] <= e:
                count += 1
                return
            elif s[mid] < s:
                end = mid -1
            elif s[mid] > e:
                start = mid + 1



for i in d:
    bsearch(i)