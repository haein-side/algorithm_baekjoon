def solution(a, b):
    end = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    
    for i in range(a):
        days += end[i]
    days += b
    
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    answer = day[days % 7]
    return answer