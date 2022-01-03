# #  실습 2C-5
# # 1부터 n까지의 정수의 합 구하기
# def sum_1ton(n):
#     sum = 0
#     for i in range(n):
#         sum += i+1
#     return sum

# x = int(input('x의 값을 입력하세요'))
# print(f'1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.')


# # 실습 2C-6
# x = [11,22,33,44,55]
# print('x=', x)
# index = int(input('업데이트할 인덱스를 선택하세요:'))
# value = int(input('새로운 값을 입력하세요:'))

# def change(lst, idx, val):
#     x[idx] = val
#     return x

# print(f'x={change(x,index,value)}')

# # 실습 2-8
# counter = 0 # 나눗셈의 횟수를 카운트

# for i in range(2,1001):
#     for j in range(2,i):
#         counter += 1
#         if i % j == 0 :
#             break
#     else : print(i) # for else 문 : 중간에 for문이 break 등으로 끊기지 않고 끝까지 수행되었을 때 실행되는 else문
#                     # 참고 : https://harryp.tistory.com/317

# print(f'나눗셈을 실행한 횟수 : {counter}')

x = [[1,2,3], [4,5,6]]
y = x.copy()

x[0][1] = 9

print(x)
print(y)

import copy
x = [[1,2,3], [4,5,6]]
y = copy.deepcopy(x)

x[0][1] = 9

print(x)
print(y)
