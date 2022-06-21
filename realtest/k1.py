def solution(survey, choices):
    tmp = ['RT', 'CF', 'JM', 'AN']
    result = {'R': 0, 'T': 0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    choose = {1:3, 2:2, 3:1, 5:1, 6:2, 7:3}

    for i in range(len(survey)):
        first = survey[i][0]
        second = survey[i][1]
        c = choose.get(choices[i]) # 점수
    
        if choices[i] <= 3:
            result[first] = result.get(first) + c
        if choices[i] > 4:
            result[second] = result.get(second) + c
    answer = ''
    for i in range(4):
        if result.get(tmp[i][0]) > result.get(tmp[i][1]):
            answer += tmp[i][0]
        elif result.get(tmp[i][0]) < result.get(tmp[i][1]):
            answer += tmp[i][1]
        else:
            answer += tmp[i][0]
    
    return answer