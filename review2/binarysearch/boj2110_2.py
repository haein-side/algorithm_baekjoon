# 현진 언니 코드
from sys import stdin
input = stdin.readline

n, c = map(int, input().split())
houses = list(int(input()) for _ in range(n))

houses.sort()

start = 1
end = houses[-1] - houses[0]
res = 0
while start <= end:
    width = (start+end)//2
    current = houses[0]
    c_count = 1

    # 이렇게 하면 가장 작은 값이 나올수밖에 없다. 생각 잘못함
    # for i in range(1,n):
    #     if houses[i] - houses[i-1] >= width:
    #         c_count += 1
    
    for i in range(1,n):
        if houses[i] >= current + width:
            current = houses[i]
            c_count += 1

    if c_count < c:
        end = width-1
    else:
        start = width+1
        res = width

print(res)

