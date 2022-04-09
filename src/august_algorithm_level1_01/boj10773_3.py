import sys

k = int(sys.stdin.readline())
s = []

def sol(n):
    global s
    if n != 0:
        s.append(n)
    elif n == 0: # n이 0인 경우
        s.pop()

for i in range(k):
    sol(int(sys.stdin.readline()))

print(sum(s))