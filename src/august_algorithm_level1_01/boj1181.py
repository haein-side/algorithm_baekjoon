n = int(input())
word = []

for i in range(n):
    s = input()
    if s not in word : # 중복 없애고 word 리스트에 append
        word.append(s)

list = [None] * len(word)

for i in range(len(word)): # list에 중복 없는 word 리스트 원소와 길이 넣어줌
    list[i] = [word[i], len(word[i])] # 리스트를 원소로 하는 리스트

# [['but', 3], ['wont', 4], ['i', 1], ['b', 1]]

list.sort(key=lambda x: (x[1], x[0])) # 두번째 원소 기준으로 오름차순 정렬

# print(list)

#[['i', 1], ['b', 1], ['but', 3], ['wont', 4]]

# for i in range(len(list)-1):
#     if list[i][1] == list[i+1][1] :
#        if list[i][0] > list[i+1][0] : # 같은 수의 원소일 때 사전 순 정렬
#            list[i] = list[i+1]

#[['b', 1], ['i', 1], ['but', 3], ['wont', 4]]        

for i in range(len(list)):
    print(list[i][0])