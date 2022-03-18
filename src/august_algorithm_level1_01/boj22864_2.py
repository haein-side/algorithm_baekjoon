import sys
a, b, c, m = map(int, sys.stdin.readline().split())

w = 0
p = 0
h = 0

if a > m :
    print(0)
else:
    for i in range(1, 25):
        if p + a <= m:
            p += a
            w += b
        else:
            if p - c >= 0:
                p -= c
            else:
                p = 0
    print(w)
