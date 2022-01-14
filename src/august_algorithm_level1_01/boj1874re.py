n = int(input())
count = 0
stack = []
result= []
no = True

# 반복문을 사용할 때는 한 개당 몇 개의 반복을 거쳐야 하는지 
# 구조를 생각해보고 작성해야 함

for i in range(n):
    target = int(input())
    
    while count < target:
        count += 1
        stack.append(count)
        result.append("+")
    
    if stack[-1] == target :
        result.append("-")
        stack.pop()
    else :
        no = False
            
            
if no == False :
    print('NO')
else :
    print("\n".join(result))

