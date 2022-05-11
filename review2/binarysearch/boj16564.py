import sys
input = sys.stdin.readline

n, k  = map(int, input().split())
level = sorted(list(int(input()) for _ in range(n)))

def bsearch():
    start = level[0]
    end = level[-1]
    answer = -1e9

    while start <= end:
        mid = (start + end) // 2 # mid는 현재 팀 목표 레벨
        tmp = 0
        for lev in level:
            if lev < mid:
                tmp += mid - lev
        if tmp <= k:
            start = mid + 1
            answer = max(answer, mid) # 그냥 answer = mid만 해줘도 됨
            '''
            answer = mid만 해줘도 되는 이유 :
            mid 값은 start = mid + 1을 이 괄호 안에서 
            계속 더해주고 있으므로 나중에 증가함. 
            따라서 t = mid해줘도 됨
            '''
        else:
            end = mid - 1
    return answer

print(bsearch())