def solution(n):
    m = 0
    s = 0
    t = []
    while n > 0:
        m = n // 3
        s = n % 3
        t.append(s)
        n = n // 3
        
        if m == 1:
            t.append(m)
            break

    answer = 0       
    for i in range(len(t)):
        answer += (3 ** (len(t)-1-i)) * t[i]
    
    return answer