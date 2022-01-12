# 소수는 소수의 제곱근 이하로 나눴을 때 나눠떨어지지 않으면 소수가 됨

M, N = map(int, input().split())

for i in range(M, N+1, 2):
    print(i,'의 제곱근:',int(i**0.5))
    if i == 1:
        continue # continue는 for문 if문 같은 곳에서 사용 시, 다음 루프로 넘기는 역할을 함
        
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else :
        print(i)
        
# 작으면 실행이 자동으로 안됨
# list = [1,2,3,4]

# for i in range(2,-1):
#     print(list[i])
