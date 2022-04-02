ub = ""
global a
a = 0
def first(t, a):
    s1 = '\"재귀함수가 뭔가요?\"'
    s2 = '\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
    s3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
    s4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"'
    ub = "____" * a
    s1 =  ub + s1
    s2 = ub + s2
    s3 = ub + s3
    s4 = ub + s4
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    if a == t-1:
        s5 = '\"재귀함수가 뭔가요?\"'
        s6 = '\"재귀함수는 자기 자신을 호출하는 함수라네\"'
        s7 = "라고 답변하였지."
        ub = "____" * (a+1)
        s5 =  ub + s5
        s6 = ub + s6
        s7 = ub + s7
        s8 = s5 + "\n" + s6 + "\n" + s7
        return print(s8)
    else:
        a += 1
        first(t, a)

def end(t,a):
    e1 = "라고 답변하였지."
    ub = "____" * t
    if t == a:
        return print("라고 답변하였지.")
    else:
        print(ub + e1)
        end(t-1, a)

t = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
first(t, a)
end(t-1, a)



