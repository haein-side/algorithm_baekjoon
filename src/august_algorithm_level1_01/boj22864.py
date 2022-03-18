import sys
a, b, c, m = map(int, sys.stdin.readline().split())

h = 0
w = 0
p = a*h

while h <= 24:
    print(a, p, h, w)
    if p <= m:
        # h += 1
        w += 1
        p = a * (h+1)
    else:
        p = a*(h-1)-c
        print(1)
