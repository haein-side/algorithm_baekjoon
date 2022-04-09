import sys

t = int(sys.stdin.readline())

def sol(n):
    a = []
    b = []
    c = []
    for i in range(len(n)):
        if n[i] == "(":
            a.append("(")
        elif n[i] == ")":
            b.append(")")
        c.append(n[i])
    if len(a) != len(b):
        print("NO")
    elif len(a) == len(b):
        count = 0
        answer = 0
        while len(c) > 0:
            if c[-1] == ")":
                c.pop()
                count += 1
            if c[-1] == "(":
                c.pop()
                count -= 1
            if count < 0:
                answer = 1
                break
        if answer == 0:
            print("YES")
        else:
            print("NO")
        
for i in range(t):
    sol(sys.stdin.readline().strip())