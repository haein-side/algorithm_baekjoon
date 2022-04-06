import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card = []
result = []
cur = '' # 현재 뽑은 카드
for i in range(n):
    card.append(sys.stdin.readline().strip())

def splice(card, n):
    return card[0:n] + card[n+1:len(card)]

def setCards(card, k):
    global cur
    curlen = len(card) # 뽑힌 것들 제외한 리스트의 길이
    
    if k <= 0: # 카드 다 뽑았을 때
        result.append(cur) # 현재의 문자열을 더해줌
        return
    
    for i in range(curlen):
        cur += card[i]
        setCards(splice(card,i), k-1)
        cur = ''

setCards(card, k) 
print(len(set(result)))
print(set(result))