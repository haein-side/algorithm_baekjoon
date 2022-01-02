# sen = input()

# word = [0]*len(sen)


# for i in sen :
#   for j in range(len(sen)) :
#     if i == sen[j] or (max(ord(sen[j]),ord(i)) - min(ord(sen[j]),ord(i)) == 32):
#       # word[i] += 1
#       # print(i)
#       word[sen.index(i)] = word[sen.index(i)] + 1

# for i in range(len(word)) :
#   num =0
#   if max(word) == word[i] :
#     num +=1
#   if num >= 2 :
#     print("?")
#   else :
#     print(sen[word.index(max(word))])


# # 두 번째 시도
# word = input()
# list = list(word)

# result = ""
# num = 0

# while True :
#   sum = 0
#   alpha = list[0]
  
#   sum += list.count(list[0])
#   sum += list.count(list[0].upper())
  
#   a = list.count(list[0])
#   b = list.count(list[0].upper())
  
#   if alpha.lower() in list :
#     for _ in range(a) :
#         list.remove(list[0])
        
#   if alpha.upper() in list :
#     for _ in range(b) :
#         list.remove(list[0].upper())
      
#   # print(sum)
#   # print(list)
  
#   if sum > num :
#     result = alpha
#     num = sum
#   if sum == num :
#     result = '?'
    
#   if len(list) == 0 :
#     break
  
# print(result.upper())



# 1157번 : 단어 공부
word = input().lower()      # word = mississipi / baaa
word_list = list(set(word)) # word_list = ['p', 'm', 'i', 's'] / ['b', 'a']
print(word_list)

cnt = []

for i in word_list:         # i = p, m, i, s / b, a
    count = word.count(i)
    cnt.append(count)       # cnt = [1, 1, 4, 4] / [1, 3]
if cnt.count(max(cnt)) >= 2: # max인 것의 갯수가 2개 이상이면 ? 출력
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())