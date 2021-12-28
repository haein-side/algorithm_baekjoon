#실습 1-1 세 정수 입력받아 최댓값 구하기
print('세 정수 최댓값을 구합니다.')

a = int(input('정수 a의 값을 입력하세요 :'))
b = int(input('정수 b의 값을 입력하세요 :'))
c = int(input('정수 c의 값을 입력하세요 :'))

maximum = max(a, b, c)

print(f'최댓값은 {maximum}입니다.')

#실습 1C-1
print('이름을 입력하세요 :', end='')
name = input()
print(f'안녕하세요 {name}님')

name = input('이름을 입력하세요 :')
print(f'안녕하세요 {name}님')

#[Do it! 실습 1-2] # 세 정수의 최댓값을 구하기

def max3(a, b, c):
    """a, b, c의 최댓값을 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum  # 최댓값 반환

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')   # [A] a > b > c
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')   # [B] a > b = c
print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')   # [C] a > c > b
print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')   # [D] a = c > b
print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')   # [E] c > a > b
print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')   # [F] a = b > c
print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')   # [G] a = b = c
print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')   # [H] c > a = b
print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')   # [I] b > a > c
print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')   # [J] b > a = c
print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')   # [K] b > c > a
print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')   # [L] b = c > a
print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')   # [M] c > b > a