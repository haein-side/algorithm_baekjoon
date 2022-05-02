import sys
input = sys.stdin.readline

n = int(input())

print(2**n -1)

def move(s, d):
    print(s, d, sep= " ")

def hanoi(n, s, d, v):
    count = 0
    if n <= 1:
        move(s, d)
        return 1

    count += hanoi(n-1, s, v, d) # 가장 큰 원반 빼고 n-1개의 원반을 보조 기둥으로 옮김
    
    count += 1
    move(s, d)
    
    count += hanoi(n-1, v, d, s) # 보조 기둥에서 목표 기둥으로 옮김
    
    return count # 왜 필요?
    
if n <= 20:
    hanoi(n, 1, 3, 2)