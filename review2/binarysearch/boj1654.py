import sys
input = sys.stdin.readline

# 잘라서 만들 수 있는 최대 랜선의 길이

k, n = map(int, input().split())
lensun = list(int(input()) for i in range(k))

start = 1
end = max(lensun)
answer = 0
def bsearch(start, end, lensun):

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in lensun:
            cnt += i // mid # 랜선 // 자르는 단위 => 몇 개?
        if cnt >= n: # 더 많이 잘림 (단위가 작은 것)
            answer = mid
            start = mid + 1 # 단위 커져야
        else: # 더 적게 잘림 (단위 큰 것)
            end = mid -1 # 단위 작아져야
    return answer
          
print(bsearch(start, end, lensun))