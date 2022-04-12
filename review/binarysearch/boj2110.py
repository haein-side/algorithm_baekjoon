import sys

N, C = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for i in range(N)]) # 정렬해서 오름차순으로 넣어줌

def sol(target):
    start = 0
    end = house[-1] - house[0]
    
    while start <= end:
        mid = (start + end) // 2 # 공유기 간 최소 거리
        count = 1 # 공유기 설치 대수
        cur = house[0] + mid # 현재 위치
        
        for i in range(1, N):
            if cur <= house[i]:
                count += 1
                cur = house[i] + mid
                
        if count >= target:
            start = mid + 1
            answer = mid
            
        elif count < target:
            end = mid - 1
            
    return answer
           

print(sol(C))
