import sys

def hanoi(n, s, d, v):
    m = '' # 어디에서 어디로 이동했는지 저장
    if n <= 1:
        m += str(s) + " " + str(d) + "\n"
        return 1
    
    count = 0
    count += hanoi(n-1, s, v, d) # n-1개를 시작 -> 보조
    
    count += 1 # 가장 큰 원반: 시작 -> 목표
    m += str(s) + " " + str(d) + "\n"
    
    count += int(hanoi(n-1, v, d, s)) # n-1개를 보조 -> 목표
    
    return m, count

n = int(sys.stdin.readline())
s = 1
d = 3
v = 2

m, count = hanoi(n, s, d, v)
print(count)
print(m)