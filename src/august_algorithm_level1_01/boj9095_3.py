import sys

t = int(sys.stdin.readline())
count = 0
def sol(n):
    count = 0
    if n == 0:
       return 1
    if n < 0:
        return 0
    for i in range(1, 4):
        count += sol(n-i) # 여기로 다시 와서 쌓이는 것
    return count 

for i in range(t):
    a = int(sys.stdin.readline())
    print(sol(a))