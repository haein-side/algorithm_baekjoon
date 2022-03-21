def solution(d, budget):
    total = 0
    count = 0
    answer = 0
    d = sorted(d)
    
    if d[0] <= budget:
        count = 1
        total = d[0]
        d.remove(d[0])
        
        for i in range(len(d)): 
            if d[i] != -1 and (budget - total) >= d[i]:
                total += d[i]
                count += 1
                d[i] = -1
                print(d)
        answer = count
    else:
        answer = 0
    
    
    return answer

print(solution([2,2,3,3], 10))