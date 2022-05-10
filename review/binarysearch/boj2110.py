import sys

N, C = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for i in range(N)]) # 정렬해서 오름차순으로 넣어줌

def sol(target):
    start = 0
    end = house[-1] - house[0]
    
    while start <= end:
        mid = (start + end) # 공유기 간 최소 거리
        count = 1 # 공유기 설치 대수
        cur = house[0] + mid # 현재 위치
        
        for i in range(1, N): 
            # 현재 위치보다 집이 더 뒤에 있으면 ?
            if cur <= house[i]:
                count += 1
                # 현재 위치를 갱신
                cur = house[i] + mid
                
        if count >= target: # 원하던 공유기보다 많은 수를 얻을 수 있었음
            start = mid + 1 # 공유기 간 최소 거리를 늘림
            answer = mid
            
        elif count < target: # 원하던 공유기보다 적은 수를 얻었다면
            end = mid - 1    # 공유기 간 최대 거리를 늘림
            
    return answer
           

print(sol(C))
