# 1번
def solution(survey, choices):
    answer = ''

    score_table = {char:0 for char in "RTCFJMAN"}
    # print(score_table)

    for s,c in zip(survey, choices):
         # zip() 함수는 여러 개의 순회 가능한 객체를 인자로 만들고, 
         # 각 객체가 담고 있는 원소들을 튜플의 형태로 차례로 접근할 수 있는 반복자를 반환
        if c < 4: # 비동의
            score_table[s[0]] += 4-c
        elif c > 4: # 동의
            score_table[s[1]] += c-4

    for t in ['RT', 'CF', 'JM', 'AN']:
        if score_table[t[0]] >= score_table[t[1]]:
            answer += t[0]
        else:
            answer += t[1]
        
    return answer