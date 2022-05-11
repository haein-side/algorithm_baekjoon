import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
sade = list(map(int, input().split()))
ani =  [list(map(int, sys.stdin.readline().split())) for i in range(n)]

sade.sort()

def bsearch():
    cnt = 0
    # 동물 기준으로 사대 찾기
    for x, y in ani: # 동물의 x축, y축 좌표
        if y > l: # 동물이 사정거리보다 높은 곳에 있음 사냥 X
            continue
        s = x+y-l # 동물별로 사냥되려면 사대가 있어야 하는 범위
        e = x-y+l 

        # 검색 대상: 사대
        start = 0
        end = m - 1

        while start <= end:
            mid = (start + end) // 2

            if s <= sade[mid] <= e:
                cnt += 1 # 해당 동물에 대한 사대 찾았으므로 cnt += 1
                break
            elif sade[mid] < s: # 사대가 있는 곳이 최솟값보다 작을 때
                start = mid + 1
            elif sade[mid] > e:
                end = mid - 1
    return cnt

print(bsearch())
            