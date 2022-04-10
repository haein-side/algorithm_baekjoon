import sys

n = sys.stdin.readline()

i = 0
arr = [] # 스택 쌓기
t = 1 # t가 1로 유지될 때 제대로 된 괄호인 것
while i <= len(n)-1:
    if n[i] == "[" or n[i] == "(":
        arr.append(n[i])
    else:
        if n[i] == "]":
            if arr[-1] == "[":
               arr.pop()
            else:
                t = 0 # t가 0이 되면 제대로 된 괄호가 아닌 것
                print(0)
                break
        elif n[i] == ")":
            if arr[-1] == "(":
                arr.pop()
            else:
                t = 0
                print(0)
                break
    i += 1
    
answer = 0
stack = []
tmp = 1
res = 0
if t == 1:
    for i in range(len(n)):
        if n[i] == "(":
            tmp *= 2
            stack.append(n[i])
        elif n[i] == "[":
            tmp *= 3
            stack.append(n[i])
        
        elif n[i] == ")":
            if not stack or stack[-1] == "[":
                res = 0 # 제대로 된 괄호 아닌 경우
                break
            if n[i-1] == "(":
                res += tmp # 짝을 찾았으므로 최종 결과에 더해줌
            tmp //= 2 
            stack.pop() # 짝을 찾았으므로 stack에서 pop을 해줌
        
        else: # n[i] == "]"
            if not stack or stack[-1] == "(":
                res = 0 # 제대로 된 괄호 아닌 경우
                break
            if n[i-1] == "[":
                res += tmp
            tmp //= 3
            stack.pop()
    print(res)