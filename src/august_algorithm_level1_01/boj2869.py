import sys

a, b, v = map(int, sys.stdin.readline().split())
height = 0
day = 0

while True:
    height += a
    day += 1
    if height >= v:
        break
    else:
        height -= b

print(day)