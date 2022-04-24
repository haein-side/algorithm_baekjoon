import sys

from numpy import sort
input = sys.stdin.readline

n, m, k = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse = True)

sum = 0
while m > 0:
    for i in range(k):
        sum += num[0]
        m -= 1
    sum += num[1]
    m -= 1

print(sum)