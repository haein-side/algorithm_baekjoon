import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted(list(int(input()) for _ in range(n)))

def binary_search(target):
    start = 0 # 두 공유기 사이에 가장 인접한 거리의 최소값
    end = house[-1]- house[0] # 두 공유기 사이에 가장 먼 거리
    ans = 0
    while start <= end:
        mid = (start + end) // 2 # 현재 구해 놓은 두 공유기 사이에 가장 먼 거리
        count = 1
        cur = house[0] # 현재 위치
        tmp = float('inf')

        for i in range(1, n): # 두번째 집부터 시작
            if cur + mid <= house[i]: # 현재 위치 + 공유기 사이의 거리 <= 다음에 공유기 놓을 수 있는 집 위치
                count += 1 # 일단 놓음
                tmp = min(tmp, house[i]-cur) # 놓을 수 있는 집 - 현재 위치 -> 최소 거리인지 확인
                cur = house[i] # 놓을 수 있는 집을 현재 위치로 갱신
        
        if count < c: # 공유기의 개수 < 목표 -> 거리 줄여야
            mid = end - 1
        elif count >= c: # 공유기의 개수 >= 목표 -> 거리 늘려야
            mid = start + 1
            ans = max(ans, tmp) # 현재 구한 것의 최소 거리
    return ans

binary_search(c)