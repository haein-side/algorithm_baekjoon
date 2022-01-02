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

# 실습 2-1
sum = 0

for i in range(5) : #0,1,2,3,4 가 i로 들어감
    n = int(input(f'{i+1}번 학생의 점수를 입력하세요:'))
    sum += n
print(f'합계는 {sum}입니다.')
print(f'평균은 {sum/5}입니다.')

list05 = list('ABC')
list06 = list([1,2,3])
list07 = list((1,2,3))
list08 = list({1,2,3})
list09 = list(range(5))
list10 = list(range(3,8))
list11 = list(range(3,9,2))
print(list05)
print(list06)
print(list07)
print(list08)
print(list09)
print(list10)
print(list11)

# 리스트의 원소의 개수는 반드시 리스트를 만들기 전에 결정해야 함
# 그러나 리스트의 원소값은 None으로 정해두지 않을 수도 있음!

list12 = [None] * 5

print(list12)


x = [11,22,33,44,55,66,77]

print(x[0:2])
print(x[0:6:2])
print(x[-5:-2])
x[-4] = 3.14
print(x)

p = [1,2,3]
a,b,c = p
print(a)