import sys
n, m = map(int, sys.stdin.readline().split())
tlist = list(map(int, sys.stdin.readline().split()))


def bsearch(start, end, target): # mid는 절단기의 길이
    if start > end :
        return end
    
    mid = (start + end) // 2
    
    a = 0 # 절단기에 자르고 남은 나무 길이
    for i in tlist:
        if i >= mid:
            a += i - mid
    
    if a == target: # 절단기에 자르고 남은 나무 길이와 원하는 나무 길이가 같을 때
        return mid
    if a > target: # 절단기에 자르고 남은 나무 길이가 원하는 나무 길이보다 길 때는 덜 잘라야 하므로 절단기 길이 길게
        start = mid + 1
    if a < target:
        end = mid - 1
    
    # 해당 함수 자체에서 리턴값이 mid 아니면 end였으므로 그 리턴값을 가져오는 것
    return bsearch(start, end, target) # 제일 처음에 돌 때 리턴해주는 값이 있어야 하므로 (절단기 길이인 mid값) return하는 것
    
print(bsearch(0, max(tlist), m))