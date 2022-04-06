import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card = []
result = []
cur = [] # 현재 뽑은 카드
for i in range(n):
    card.append(sys.stdin.readline().strip())

def splice(card, n):
    return card[0:n] + card[n+1:len(card)]

def setCards(card, k):
    global cur
    curlen = len(card) # 뽑힌 것들 제외한 리스트의 길이
    
    if k <= 0: # 카드 다 뽑았을 때
        result.append(''.join(cur)) # cur[0]만 하면 처음으로 뽑은 카드만 넣어주게 되므로 안 됨
        return                      # cur 리스트에 있는 모든 원소들을 하나로 이어서 문자열로 만들어야
    
    for i in range(curlen):
        cur.append(card[i]) # 뽑은 카드를 cur 리스트에 넣어줌 ['1', '12']
        setCards(splice(card,i), k-1)
        cur.pop()

setCards(card, k) 
print(len(set(result)))
# print(set(result))