import sys
m, n, l = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
d = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    d[i] = list(map(int, sys.stdin.readline().split()))
      
d = sorted(d)
dict = {} # x축 좌표에서 가질 수 있는 최대 사정거리 : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 7: 0, 8: 0, 9: 0}
for i in range(n):
    dict[d[i][0]] = 0 

c = [] # 최대 점 : [[6, 4], [1, 4], [4, 4], [9, 4]]
for i in s:
    c.append([i, l])

def rec(x, y): # 변화된 dict : {1: 4, 2: 3, 3: 3, 4: 4, 5: 3, 7: 3, 8: 3, 9: 4}
    if y <= 0:
        return
    if x < d[0][0]:
        return
    if x > d[len(d)-1][0]:
        return
    
    if x in dict.keys():
        tmp = max(dict.get(x), y) # max 값인 것을 넣어줌
        dict[x] = tmp
    
    rec(x-1, y-1)
    rec(x+1, y-1)    
    
for i in range(len(c)):
    rec(c[i][0], c[i][1]) 

count = 0
for i in range(len(d)):
    if dict.get(d[i][0]) >= d[i][1]:
        count += 1
    
print(count)

# 인덱스가 x 좌표이고 y 좌표가 그 값이라고 할 때?