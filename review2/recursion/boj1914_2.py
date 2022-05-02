import sys
input = sys.stdin.readline

n = int(input())

print(2**n-1)

def move(s, d):
    print(s, d, sep = " ")


def hanoi(n, s, d, v):
    if n <= 1:
        move(s,d)
        return 1
    count = 0
    
    count += hanoi(n-1, s, v, d)
    
    count += 1
    move(s, d)
    
    count += hanoi(n-1, v, d, s)
    
    return count

hanoi(n, 1, 3, 2)