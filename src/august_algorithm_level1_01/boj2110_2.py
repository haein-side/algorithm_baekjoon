import sys
import itertools

n, s = map(int, sys.stdin.readline().split())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))

def bsearch(m, s):
    m.sort()
    start = 0
    end = m[-1] - m[0] # 두 집 사이의 거리 중 최댓값
    ans = 0
    
    while start <= end:
        mid = (start + end) // 2
        count = 1
        cur = m[0]
        tmp = float('inf')
        
        # 공유기를 몇 개 놓을 수 있는지 구하기
        for i in range(1, len(m)):
            if cur + mid <= m[i]:
                tmp = min(m[i]-cur, tmp) # m[i]는 공유기 둘 수 있는 곳, cur는 이미 공유기 둔 곳 // 거리 중 최솟값을 구하기 위해 비교
                count += 1
                cur = m[i] # 공유기를 두었으므로 cur를 m[i]로 갱신함
        
        # 공유기 개수에 따라 end, start 이진탐색
        if count < s: # 공유기 설치 더해야 => 간격 더 짧게 해야
            end = mid - 1
        elif count >= s: # 공유기 설치 완료 or 더 많이 됨 => 간격 더 길게 해야
            start = mid + 1
            ans = max(ans, tmp)
    
    # while문이 끝난 이후 ans 리턴        
    return ans


print(bsearch(m, s))