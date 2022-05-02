import sys
input = sys.stdin.readline
from itertools import permutations

# 풀이 1. by permutations & set
# 순열 : 순서 고려 
# from itertools import permutations 
# permutations(c, k) : c라는 데이터 중에서 k개를 순서를 고려해서 뽑음

# set : 중복 없애기

n = int(input())
k = int(input())
c = list(int(input()) for _ in range(n)) # 카드

checked = list(permutations(c, k))
new = []
for i in range(len(checked)):
    w = ''
    for j in range(k):
        w += str(checked[i][j])
    new.append(w)
print(len(set(new)))