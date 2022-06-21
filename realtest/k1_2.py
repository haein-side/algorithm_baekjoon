# 카카오 2022 상반기 인턴 1번 문제 리팩토링
'''
처음 풀 땐 각 질문별 점수를 choose라는 딕셔너리에 넣어주고 
그 키 값에 해당되는 값을 점수로 가져왔지만,
사실 3번 이하의 질문들은 각각 4에서 질문의 번호를 빼준 것이 점수였고,
5번 이상의 질문들은 각각 질문의 번호에서 4를 뺀 것이 점수였다. 
따라서 해당 부분을 반영하여 문제를 다시 풀어보았다.
또한 딕셔너리에서 한 번에 값을 0으로 초기화를 해줄 때, 
score_table = {char: 0 for char in "RTCFJMAN"} 으로 해줄 수 있다.
'''
def solution(survey, choices):
    answer = ''

    result = {char:0 for char in survey}

    for s, c in zip(survey, choices):
        if c < 4:
            result[s[0]] += 4-c
        elif c > 4:
            result[s[1]] += c-4

    for t in ['RT', 'CF', 'JM', 'AN']:
        if result[t[0]] >= result[t[1]]:
            answer += t[0]
        else:
            answer += t[1]
    
    return answer