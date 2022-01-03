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

# x = [[1,2,3], [4,5,6]]
# y = x.copy()

# x[0][1] = 9

# print(x)
# print(y)

# import copy
# x = [[1,2,3], [4,5,6]]
# y = copy.deepcopy(x)

# x[0][1] = 9

# print(x)
# print(y)

# # 선형 탐색
# from typing import Any,Sequence

# num = int(input('원소 수를 입력하세요.: ')) 
# x = [None] * num

# for i in range(num):
#     x[i] = int(input(f'x[{i}]:'))
    
# ky = int(input('검색할 값을 입력하세요'))

# # while 문을 이용
# def seq_search(a:Sequence, key: Any) -> int:
#     i = 0
    
#     while True :
#         if a[i] == key :
#             return i
#         if i == len(a) : # 인덱스 번호가 한바퀴를 다 돌고 전체 인덱스를 초과했을 때
#             return -1    # return i 했다면 바로 break 돼서 함수 나감
#         i += 1

# # for문을 이용
# def  seq_search1(a:Sequence, key:Any) -> int:
#     for i in range(num):
#         if a[i] == key :
#             return i
#     return -1

# #idx = seq_search(x,ky)
# idx = seq_search1(x,ky)

# if idx == -1 :
#     print('검색값을 갖는 원소가 존재하지 않음')
# else :
#     print(f'검색값은 x[{idx}]에 있습니다.')

# # 실습 3C-1
# from ssearch_while import seq_search

# print('실수를 검색')
# print('주의 : "End"를 입력하면 종료')

# number = 0
# x = []

# while  True :
#     s = input(f'x[{number}]:')
#     if s == "End" :
#         break
#     # x의 크기가 정해질 수 없을 때는 .append() 메소드 이용
#     x.append(float(s)) # 실수를 검색하는 것이므로 input() 받은 걸 float() 함수로 형변환
#     number += 1

# ky = float(input('검색할 값을 입력하세요.:'))

# idx = seq_search(x,ky)

# if idx == -1 :
#     print('검색값을 갖는 원소가 없음')
# else:
#     print(f'검색값은 x[{idx}]에 있음')

# 실습 3-3 
# 선형 검색 알고리즘을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq:Sequence, key:Any) -> int :
    a = copy.deepcopy(seq)
    a.append(key)
    k = 0
    
    for i in range(len(a)):
        if a[i] == key :
            k = i
            break
    #print(f'{k} {len(a)}')
    if k == len(a)-1 : # 인덱스 번호가 새로 만든 a 리스트의 마지막 원소에 해당할 때..
        return -1
    else :
        return k    
    
num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
x = [None] * num                           # 원소 수가 num인 배열을 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받기

idx = seq_search(x, ky)                     # ky값과 같은 원소를 x에서 검색

if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')