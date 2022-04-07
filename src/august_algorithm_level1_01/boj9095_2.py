import sys

t = int(sys.stdin.readline())
count = 0
def sol(n):
    global count
    if n == 0:
       count += 1
    if n < 0:
        return
    for i in range(1, 4):
        sol(n-i) 

for i in range(t):
    a = int(sys.stdin.readline())
    sol(a)
    print(count)
    count = 0