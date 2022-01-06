n = int(input())
word = []

for i in range(n):
    s = input()
    if s not in word :
        word.append(s)

list = [None] * len(word)

for i in range(len(word)):
    list[i] = [word[i], len(word[i])]

# print(list)
# print(word)
# list [['but', 3], ['wont', 4], ['i', 1]]

list.sort(key=lambda x: (x[1], x[0])) #[['i', 1], ['but', 3], ['wont', 4]]

for i in range(len(list)-1):
    if list[i][1] == list[i+1][1] :
       if list[i][0] > list[i+1][0] :
           list[i] = list[i+1]
        
for i in range(len(list)):
    print(list[i][0])