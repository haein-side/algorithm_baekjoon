import sys

n, c = map(int, sys.stdin.readline().split())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))

m = sorted(m)

def bsearch(start, end):
    
    while start <= end:
        mid = (end-start) // 2 # mid: 거리
        count = 1
        cur = m[0]
        point = [m[0]]
        minus = []
        tmp = 999999
        ans = 0
            
        for i in range(1, n):
            if m[i] > cur + mid:
                count += 1
                point.append(m[i])
                cur = m[i]
        
        for i in reversed(range(len(point)-1)):
            minus.append(m[i]-m[i+1])
            
        tmp = min(minus[-1], tmp)
        
        if count < c: # 원하는 것보다 덜 잘렸을 때 거리가 짧아야
            end = mid - 1
        if count >= c: # 원하는 것보다 더 잘렸을 때 거리가 길어야
            start = mid + 1   
            ans = max(tmp, ans)
    
    return ans



bsearch(0, m[-1]-m[0]) # 두 거리 사이의 최댓값을 end로 두기