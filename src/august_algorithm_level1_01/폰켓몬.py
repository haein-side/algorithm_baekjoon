def solution(nums):
    n = len(nums) // 2
    t = len(set(nums))
    answer = 0
    
    if t <= n :
        answer = t
    else :
        answer = n
    
    return answer