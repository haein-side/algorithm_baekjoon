import sys
M, N, L = map(int, sys.stdin.readline().split())
sade = list(map(int, sys.stdin.readline().split()))
ani = sorted([list(map(int, sys.stdin.readline().split())) for i in range(N)])

rst = 0
for x, y in ani:
    cnt = 0
    start = x + y - L
    end = L - y + x
    
    for j in sade:
        if j >= start and j <= end:
            cnt = 1
    
    if cnt > 0:
        rst += 1
    
print(rst)