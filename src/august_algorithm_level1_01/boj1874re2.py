n = int(input())
count = 0
stack = []
result= []
no = True

for i in range(n):
    x = int(input())
    
    # x 이하의 수를 stack에 push
    while count < x:
        count += 1
        stack.append(count)
        result.append("+")
    
    # stack 마지막 값과 x가 같으면 pop
    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else :
        no = False
        
if no == False :
    print('NO')
else :
    print("\n".join(result))    
