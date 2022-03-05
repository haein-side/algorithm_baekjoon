import sys

N, M = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

num.sort()

left = 0
right = max(num)
answer = 0
while left <= right:
    cnt = (left + right) // 2
    cut = 0
    for i in num:
        if i >= cnt:
            cut += i - cnt
    # if cut == M:
    #     print(cnt)
    #     break
    if cut < M:
        right = cnt -1
    else:
        answer = cnt
        left = cnt + 1
print(answer)
        
