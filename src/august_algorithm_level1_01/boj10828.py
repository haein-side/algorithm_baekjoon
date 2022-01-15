import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    order = sys.stdin.readline()
    a = order.split()[0]
    
    if a == "push":
        stack.append(int(order.split()[1]))
    elif a == "pop":
        if len(stack) > 0 :
            print(stack.pop())
        else :
            print(-1)
    elif a == "size":
        print(len(stack))
    elif a == "empty":
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif a == "top":
        if len(stack) == 0 :
            print(-1)
        else : 
            print(stack[-1])
    
