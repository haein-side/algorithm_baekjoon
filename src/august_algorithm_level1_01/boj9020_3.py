import sys
from itertools import combinations_with_replacement


nlist = [False,False] + [True]* 10002 # 먼저 만들어두기

for i in range(2, 10001):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            nlist[i] = False
            break
    else:
        nlist[i] = True

def sol(n, nlist): # 참고 블로그 https://deokkk9.tistory.com/20
    a = n//2 # 두 수의 차가 적은 수를 구하는 것이므로 입력받은 n의 중간부터 비교해 나감
    b = a
    while a > 0:
        print(nlist[a], nlist[b])
        if nlist[a] and nlist[b]:
            print(a,b)
            break
        else:
            a -= 1
            b += 1


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    sol(n, nlist)