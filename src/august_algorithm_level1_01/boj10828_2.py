import sys

t = int(sys.stdin.readline())
stack = []

def sol(n):
    global stack
    if "push" in n:
        stack.append(n.split()[1])
    if "pop" == n:
        if len(stack) == 0:
            return -1
        else:
            print(stack.pop())
    if "size" in n:
        return len(stack)
    if "empty" in n:
        if len(stack) > 0:
            return 0
        else:
            return 1
    if "top" in n:
        if len(stack) > 0:
            return stack[-1]
        else:
            return -1

for i in range(t):
    n = sys.stdin.readline().strip()
    if sol(n) != None:
        print(sol(n))