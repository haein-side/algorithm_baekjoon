def solution(dartResult):
    arr= []
    one = []
    two = []
    three = []
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            arr.append(i)
    
    one = dartResult[0:arr[0]+1]
    two = dartResult[arr[0]+1:arr[1]+1]
    three = dartResult[arr[1]+1:]

    if two[0].isdigit() == False:
        one = one + two[0]
        two = two[1:]
    if three[0].isdigit() == False:
        two = two + three[0]
        three= three[1:]
    op = {'S':1, 'D':2, 'T':3}
    onea = 0
    twoa = 0
    threea = 0
    for i in range(len(one)):
        if one[i] in op.keys():
            onea = int(one[:i]) ** op[one[i]]
    for i in range(len(two)):
        if two[i] in op.keys():
            twoa = int(two[:i]) ** op[two[i]]
    for i in range(len(three)):
        if three[i] in op.keys():
            threea = int(three[:i]) ** op[three[i]]
    
    if one[-1] == "*":
        onea = onea * 2
    elif one[-1] == "#":
        onea = onea * (-1)
    
    if two[-1] == "*":
        onea = onea * 2
        twoa = twoa * 2
    elif two[-1] == "#":
        twoa = twoa * (-1)
    
    if three[-1] == "*":
        threea = threea * 2
        twoa = twoa * 2
    elif three[-1] == "#":
        threea = threea * (-1)
    
    
    print(one, two, three, onea, twoa, threea)
    answer = onea + twoa + threea
    return answer