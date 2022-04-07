import sys
n, m = map(int, sys.stdin.readline().split())
tlist = sorted(list(map(int, sys.stdin.readline().split())))
answer = []
def bsearch(data, target): # mid는 절단기의 길이
    start = 0
    end = max(data)
    global answer
    
    while start <= end:
        mid = (start + end) // 2
        
        a = 0 # 절단기에 자르고 남은 나무 길이
        for i in tlist:
            if i >= mid:
                a += i - mid
        if a == target: # 절단기에 자르고 남은 나무 길이와 원하는 나무 길이가 같을 때
            answer.append(mid)
            return
        if a > target: # 절단기에 자르고 남은 나무 길이가 원하는 나무 길이보다 길 때는 덜 잘라야 하므로 절단기 길이 길게
            start = mid + 1
        if a < target:
            end = mid - 1
            
    return None
    
bsearch(tlist, m)
print(max(answer))