import sys
 
a, b, c = map(int, sys.stdin.readline().split())

#  지수를 매번 2로 나눠 더 작은 문제로 만들어 해결하는 분할정복 방식

def power(a, b):
    if b == 0:
        return 1
    
    x = power(a, b//2)
    
    if b % 2 == 0:
        return x * x
    else:
        return x * x * a

print(power(a, b)%c)