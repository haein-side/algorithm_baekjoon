import sys

g, s = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
ga = []
se = []

ga.append(g)
se.append(s)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    
    if a == 0:
        se.append(b)
    else:
        ga.append(b)

ga.append(0)
se.append(0)

ga = sorted(ga, reverse = True)
se = sorted(se, reverse = True)

gc = []
sc = []
for i in range(len(ga)-1):
   gc.append(ga[i]-ga[i+1])
for i in range(len(se)-1):
    sc.append(se[i]-se[i+1])

answer = max(gc) * max(sc)
    
print(answer)