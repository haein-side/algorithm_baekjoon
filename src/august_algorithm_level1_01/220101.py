area = int(input("직사각형 넓이를 입력 :"))

for i in range(1, area + 1) :
    if i * i >  area : break
    if area % i != 0 : continue 
    print(f'{i} x {area // i}')
    
    
# 실습 1-19
word = ""

for i in range(1, 13)  :
    if i != 8 :
        word.append(str(i) + " ")

print(word)

for i in range(1, 13):
    if i == 8 :
        continue
    print(i, end=" ")
print()

for i in list(range(1,8)) + list(range(9,13)):
    print(i, end= " ")
    
# 실습 1C-3
print('2자리 양수 입력하세요')

while True :
    no = int(input("값을 입력하세요 :"))
    if no >= 10 and no <= 99 :
        print(f'입력받은 정수는 {no}입니다')
        break

# 실습 1-21
print("-"*27)

for i in range(1,10) :
    for j in range(1,10):
        print(i*j, end = " ")
    print()

# 실습 1-22
n = int(input("짧은 변의 길이를 입력하세요 : "))

for i in range(n):
    print("*"*(i+1))
    
for j in range(n) :
    for k in range(j+1) :
        print("*",end = "")
    print()

# 실습 1-23
n = int(input('짧은 변의 길이를 입력하라 : '))

for i in range(n):
    for j in range(n-(i+1)):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()




