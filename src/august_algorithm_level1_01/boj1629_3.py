import sys
 
a, b, c = map(int, sys.stdin.readline().split())

def power(a, b, c):
    result = 1
    while b > 0:
        if b % 2 != 0: # 거듭제곱 해줘야 하는 지수가 홀수이면 a를 한 번 더 곱해줌
            result = (result * a) % c
        a = (a * a) % c # a를 계속 2개씩 b//2 번 곱해주면 a**b가 됨
        b = b // 2
    return result

print(power(a, b, c))