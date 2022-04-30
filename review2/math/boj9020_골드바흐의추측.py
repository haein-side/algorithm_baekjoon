import sys

input = sys.stdin.readline

t = int(input())

def sosu(halfn, j):
    a, b = 0, 0
    # halfn - 1인 수
    flag1 = False
    for i in range(2, halfn-j):
        if (halfn-j) % i == 0:
            break
    else:
        flag1 = True # 소수일 때
        a = halfn-j
    
    # halfn + 1인 수
    flag2 = False 
    for i in range(2, halfn+j):
        if (halfn+j) % i == 0:
            break
    else:
        flag2 = True # 소수일 때
        b = halfn+j
    
    if flag1 and flag2: # 둘 다 소수일 때
        print(str(a) + " " + str(b))
        return False
    else:
        return True

for i in range(t):
    n = int(input())
    
    # n을 2로 나누고 생기는 값들에 한 개는 1씩 감소시키고 한 개는 1씩 증가시키기
    # 둘 다 소수인 경우 출력
    # 소수 판별 by 에라토스테네스의 체 (하고 싶었으나 기억이 안 남)
    
    halfn = n//2
    
    i = 0
    while True:
        if not sosu(halfn, i):
            break
        i += 1
        
    
    