import sys

a, b, c = map(int, sys.stdin.readline().split())

def power(a, b, c):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % c
        a = (a * a) % c
        b = b // 2
    return result

print(power(a, b, c))