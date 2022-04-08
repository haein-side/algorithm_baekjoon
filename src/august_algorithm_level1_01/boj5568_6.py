# 재귀 프로젝트 1
# 뽑은 카드를 cur리스트에 넣어주고 그걸 가지고 뽑는 게 부족했음
# 아직 이해가 안됨...

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
clist = []

for i in range(n):
    clist.append(sys.stdin.readline().strip())

def pick(card, k):
    N = len(card)
    answer = []
    if k == 0:
        return "".join(card)
    
    for i in range(N):
        card = card[0:i] + card[i+1:N]
        answer.append(pick(card, k-1))
    
    return answer

print(pick(clist, k))

