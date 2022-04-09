N, K = map(int, input().split())
level = sorted([int(input()) for _ in range(N)])

def cal(level, mid): # 레벨 리스트, 올릴 수 있는 레벨 총합, 팀 목표 레벨
    sum = 0
    for i in level:
        if i < mid: # 팀 목표 레벨보다 레벨이 적을 때
            sum += mid - i
    return sum
            
def bsearch(level):
    level.sort()
    start = level[0]
    end = level[N-1] + K # 가장 최댓값은 level 리스트 중 가장 큰 수 + 올릴 수 있는 레벨의 총합
    result = 0
    while start <= end:
        mid = (start + end) // 2 # mid : 팀 목표 레벨
        
        if cal(level, mid) <= K: # 팀 목표 - 현재 각 캐릭터의 레벨 차의 합 <= 올릴 수 있는 레벨의 총합
            result = mid # 다음 반복문 시 mid가 변경될 수 있으므로 될 때 result 변수에 mid 값을 넣어줌
            start = mid + 1 # 수를 키워야 하므로 start를 크게 만들어주기 위해 start = mid 대입
        elif cal(level, mid) > K:
            end = mid - 1 # 수를 작게 해줘야 하므로 end를 작게 만들어주기 위해 end = mid 대입
    
    return result

print(bsearch(level))