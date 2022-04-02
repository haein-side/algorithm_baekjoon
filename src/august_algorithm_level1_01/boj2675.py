import sys

def sol(a, b):
    answer = ''
    
    for i in range(len(b)):
        answer = answer + b[i]*a
    return answer

t = int(sys.stdin.readline())

for i in range(t):
    a, b = sys.stdin.readline().split()
    a = int(a)
    print(sol(a, b))
