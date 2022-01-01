sen = input()


word = [0]*len(sen)


for i in sen :
  for j in range(len(sen)) :
    if i == sen[j] or (max(ord(sen[j]),ord(i)) - min(ord(sen[j]),ord(i)) == 32):
      # word[i] += 1
      # print(i)
      word[sen.index(i)] = word[sen.index(i)] + 1

for i in range(len(word)) :
  num =0
  if max(word) == word[i] :
    num +=1
  if num >= 2 :
    print("?")
  else :
    print(sen[word.index(max(word))])