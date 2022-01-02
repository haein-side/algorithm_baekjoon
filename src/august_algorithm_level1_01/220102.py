# # 실습 2-4
# import random
# from max import max_of

# print('난수의 최댓값을 구함')

# num = int(input('난수의 개수:'))
# list = [None]*num

# lo = int(input('난수의 최솟값:'))
# hi = int(input('난수의 최댓값:'))

# for i in range(num):
#     list[i]= random.randint(lo,hi)

# print(list)

# print(f'이 가운데 최댓값은 {max_of(list)}입니다.')

#  # [Do it! 실습 2-5] 배열 요소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

# from max import max_of

# t = (4, 7, 5.6, 2, 3.14, 1)
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']

# print(f'{t}의 최댓값은 {max_of(t)}입니다.')
# print(f'{s}의 최댓값은 {max_of(s)}입니다.')
# print(f'{a}의 최댓값은 {max_of(a)}입니다.')


# # [Do it! 실습 2C-2] 리스트의 모든 원소를 ​​enumerate 함수로 스캔하기

x = ['John', 'George', 'Paul', 'Ringo']
x.reverse()
print(x)
# # print(x[::-1])

# for i, name in  enumerate(x,1) :
#     print(f'x[{i}] = {name}')

