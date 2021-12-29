#01.알고리즘 기초 01-2 반복하는 알고리즘

#실습 1-7
#1부터 n까지 정수의 합 구하기1(while문)

print("1부터 n까지의 합을 구합니다")

n = int(input('n값을 입력하세요 :'))

i = 1
sum = 0

while True : 
    sum += i
    i += 1
    if i > n :
        break
    
# while i <= n:  # i가 n보다 작거나 같은 동안 반복
#     sum += i   # sum에 i를 더함
#     i += 1     # i에 1을 더함
    
print(f"1부터 {n}까지의 정수의 합은 {sum}입니다.")

#실습 1-8
print("1부터 n까지의 합을 구합니다")

n = int(input('n값을 입력하세요 :'))
sum = 0

for i in range(1, n+1) :
    sum += i

print(f"1부터 {n}까지의 정수의 합은 {sum}입니다.")

# 실습 1-9
# a부터 b까지의 정수의 합을 구하기
print("a부터 b까지의 정수의 합을 구합니다")
a = int(input('a값을 입력하세요 :'))
b = int(input('b값을 입력하세요 :'))

min = 0
max = 0

if a <= b :
    min = a
    max = b
    #a,b = a,b
else :
    min = b
    max = a
    #a,b = b,a


sum = 0

for i in range(min, max+1) :
    sum += i
    
print(f"{a}부터 {b}까지의 정수의 합은 {sum}입니다.")

