import sys
x, y, w, h = map(int, sys.stdin.readline().split())

a = min (h-y, w-x, x, y)

print(a)