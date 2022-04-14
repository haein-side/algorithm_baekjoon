import sys

w = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
word = [] # 문자열
for i in range(len(w)):
    word.append(w[i])
target = [] # 폭발물
for i in range(len(t)):
    target.append(t[i])
    
print(target)

for i in range(len(word)-1, -1, -1):
    print(word)
    if word[i] == target[-1]:
        # print('일치')
        cnt = 0
        for j in range(len(target)-2, -1, -1):
            # print('타겟',target[j], '단어', word, 'j', j)
            if word[i-(len(target)-1-j)] == target[j]:
                cnt += 1
        if cnt == len(target) - 1:
            # print(i,'번째', word[i])
            for k in range(i, i-len(target), -1):
                # print(k,'번째', word[k])
                word.pop(k)
                

print(word)