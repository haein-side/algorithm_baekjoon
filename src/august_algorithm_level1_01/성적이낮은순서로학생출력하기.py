import sys

n = int(sys.stdin.readline())
s = []

for i in range(n):
    a, b = sys.stdin.readline().split()
    s.append([a, b])

s = sorted(s, key = lambda x:(x[1]))

for i in s:
    print(i[0], end = " ")