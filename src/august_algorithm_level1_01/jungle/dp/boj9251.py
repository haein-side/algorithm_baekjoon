# LCS  (혼자 풀어본 것 - 오답)
import sys
input = sys.stdin.readline

w = list(input().strip())
t = list(input().strip())

res = 0
p = 0

for i in range(len(w)):
    for j in range(len(t)):
        if j > p:
            if w[i] == t[j]:
                res += 1
                p = j
                # print(j, t[j])
                break

if w[0] == t[0]:
    res += 1

p = len(t)-1
res2 = 0      
for i in range(len(w)-1, -1, -1):
    for j in range(len(t)-1, -1, -1):
        if j < p:
            if w[i] == t[j]:
                res2 += 1
                p = j
                # print(j, t[j])
                break

if w[-1] == t[-1]:
    res2 += 1
    
print(max(res, res2))