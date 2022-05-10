import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

def binary_search(target):
    start = 0                   # 가장 인접한 거리의 최소 거리
    end = houses[-1]-houses[0]  # 가장 인접한 거리의 최대 거리
    res = 0

    while start <= end:
        cnt = 1
        crt = houses[0]
        width = (start + end) // 2 # 가장 인접한 거리
        
        for i in range(1, n):
            if crt + width <= houses[i]: # 공유기를 놓을 수 있으면
                cnt += 1
                crt = houses[i] # 어차피 width는 가장 인접한 거리이므로 갱신해줄 필요 없음!
        
        if cnt < c:
            end = width - 1
        else:
            start = width + 1
            res = width
    
    return res

print(binary_search(c))
