import sys

m, n, l = map(int, sys.stdin.readline().split())
sade = list(map(int, sys.stdin.readline().split())) # 사대의 x축 좌표 리스트
animal = list(map(int, sys.stdin.readline().split()) for _ in range(n)) # 2차원 배열 [x축, y축]

sade.sort()

# 동물 기준으로 사대 찾기
count = 0
for x, y in animal: # 동물의 x축, y축 좌표
    if y > l: # 동물이 사정거리보다 높은 곳에 있으면 사냥 X (반복문 조기 종료 조건)
        continue 
    s = x+y-l # x, y 좌표별로 s, e를 계산 (동물별 사냥되려면 사대가 있어야 하는 범위)
    e = x-y+l
    
    # 검색대상 : 사대
    start = 0
    end = len(sade)-1
    
    while start <= end:
        mid = (start + end) // 2
        
        if sade[mid] >= s and sade[mid] <= e:
            count += 1 # 해당 동물에 대한 사대 찾았으므로 count += 1
            break
        elif sade[mid] < s: # 사대가 있는 곳이 동물에 대한 사정 거리보다 작음 => 사대가 있는 곳을 크게 해야
            start = mid + 1
        elif sade[mid] > e: # 사대가 있는 곳이 동물에 대한 사정 거리보다 큼 => 사대가 있는 곳을 작게 해야
            end = mid - 1

print(count)
        
            
            
     