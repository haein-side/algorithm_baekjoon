def count(level, mid):
    t = 0
    for i in level:
        if i >= mid:
            break
        t += mid-i
    return t

N, K = map(int, input().split())
level = sorted([int(input()) for _ in range(N)])
start, end = min(level), max(level)+K
result = 0
while start <= end:
    mid = (start+end)//2
    if count(level, mid) <= K:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)