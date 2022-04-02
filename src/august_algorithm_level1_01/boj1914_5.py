import sys

def move(s,d):
    print(s, d, sep =" ")

def hanoi(n, s, d, v):
    m = '' # 어디에서 어디로 이동했는지 저장
    if n <= 1:
        move(s, d)
        return 1
    
    count = 0
    count += hanoi(n-1, s, v, d) # n-1개를 시작 -> 보조
    
    count += 1 # 가장 큰 원반: 시작 -> 목표
    move(s,d)
    
    count += int(hanoi(n-1, v, d, s)) # n-1개를 보조 -> 목표
    
    return count

n = int(sys.stdin.readline())
s = 1
d = 3
v = 2

print(2**n-1) # 원반이 n개일 때 움직이는 횟수는 2의 n승 -1!

if n <= 20:
    hanoi(n, s, d, v) # 20 이하일 때 하노이 함수를 실행하면 move() 함수에서 알아서 print가 됨!

