T = int(input())

def sol(q):
    s = ''
    a = []
    q = q + 'X'
    for i in range(len(q)):
        if q[i] == 'O':
            s = s + 'O'
        else:
            a.append(s)
            s = ''
    midanswer = []
    for i in a:
        if len(i) > 0:
            mid = 0
            for j in range(len(i)):
                mid += (j+1)
            midanswer.append(mid)
    return sum(midanswer)



for i in range(T):
    q = input()
    
    print(sol(q))
