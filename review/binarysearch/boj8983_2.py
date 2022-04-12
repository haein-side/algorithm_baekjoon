import sys
M, N, L = map(int, sys.stdin.readline().split())
sade = sorted(list(map(int, sys.stdin.readline().split())))
ani = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

def bsearch():
    # 검색 대상 : 사대
    # 검색 타겟 : ani가 사냥되려면 사대가 위치해야 하는 범위 
    # 이진탐색 진행 방향 : 각 ani별로 사냥되려면 사대가 위치해야 하는 범위에 사대가 있는지 이진탐색으로 찾는다.
    
    # 사대의 인덱스
    cnt = 0
    for x, y in ani:
        start = 0
        end = M - 1
        a = x + y -L
        b = x - y + L
        while start <= end:
            mid = (start + end) // 2 # 현재 사대의 인덱스
            # print('사대 위치', a, b, sade[mid])
            if sade[mid] >= a and sade[mid] <= b:
                cnt += 1
                break
            elif sade[mid] < a: # 목표했던 사대의 위치보다 작은 곳에 사대가 있으면 사대가 더 큰 곳에 위치해야 함
                start = mid + 1
            elif sade[mid] > b: # 목표했던 사대의 위치보다 큰 곳에 사대가 있으면 사대가 더 작은 곳에 위치해야 함
                end = mid - 1
    
    return cnt
        

print(bsearch())
    

