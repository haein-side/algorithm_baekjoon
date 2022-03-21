def solution(left, right):
    dic = dict()

    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        dic[i] = cnt
    
    answer = 0
    
    for i in dic:
        print(dic[i])
        if dic[i] % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer