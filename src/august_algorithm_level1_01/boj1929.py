# 시간초과 풀이
# M, N = map(int, input().split())

# for i in range(M, N+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else :
#         print(i)

# [Do it! 실습 2-8] 1,000 이하의 소수를 나열하기

# counter = 0  # 나눗셈 횟수

# for n in range(3, 17):
#     for i in range(2, n):
#         counter += 1
#         if n % i == 0 :     # 나누어 떨어지면 소수가 아님
#             break           # 반복은 더 이상 불필요하여 중단
#     else:                   # 끝까지 나누어 떨어지지 않으면 다음을 수행
#         print(n)
# print(f'나눗셈을 실행한 횟수: {counter}')


# list = [1]

# for i in range(0,0):
#     print(list[i])

# [Do it! 실습 2-9] 1,000 이하의 소수를 나열하기(알고리즘 개선 1)

counter = 0           # 나눗셈 횟수
ptr = 0               # 이미 찾은 소수의 개수
prime = [None] * 500  # 소수를 저장하는 배열

prime[ptr] = 2        # 2는 소수이므로 초깃값으로 지정
ptr += 1

for n in range(3, 1001, 2):  # 홀수만을 대상으로 설정
    for i in range(1, ptr):  # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0:  # 나누어 떨어지면 소수가 아님
            break              # 반복 중단
    else:                      # 끝까지 나누어 떨어지지 않았다면
        prime[ptr] = n         # 소수로 배열에 등록
        ptr += 1

for i in range(ptr):  # ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')