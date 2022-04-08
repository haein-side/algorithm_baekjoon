import sys

n, c = map(int, sys.stdin.readline().split())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
m = sorted(m)

def bsearch(m, c):
    start = 0
    end = m[-1] - m[0]
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        count = 1
        cur = m[0]
        tmp = float('inf')
        
        for i in range(1, n):
            if cur + mid <= m[i]: # 내가 놓을 수 있는지 알아보기
                count += 1
                tmp = min(tmp, m[i]-cur) # 최소 거리를 업데이트
                cur = m[i]
        
        if count < c: # 원하는 갯수보다 적을 때 더 많이 있어야 하므로 거리 줄어야
            end = mid - 1
        if count >= c: # 원하는 갯수보다 많을 때 더 적게 있어야 하므로 거리 늘어야
            start = mid + 1
            ans = max(ans, tmp)
    
    return ans
                    
print(bsearch(m, c))