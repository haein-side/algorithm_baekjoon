def solution(sizes):
    arr = []
    g = 0
    s = 0
    arr = [sorted(size, reverse = True) for size in sizes]
    
    ga = []
    se = []
    for i in range(len(arr)):
        ga.append(arr[i][0])
        se.append(arr[i][1])
    
    answer = max(ga) * max(se)
    return answer