def solution(N, stages):
    arr = []
    for i in range(1, N+1):
        m = 0
        z = 0
        f = 0
        for j in stages:
            if i <= j:
                m += 1
            if i == j:
                z += 1
        if m == 0: f = 0
        else:
            f = z / m
        arr.append([i, f])
    
    answer = []
    temp = sorted(arr, key = lambda x: (-x[1], x[0]))
    
    for i in range(len(temp)):
        answer.append(temp[i][0])
    
    return answer