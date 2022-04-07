# 혜린님 코드
from sys import stdin
input = stdin.readline

def getcnt(num) :
    global cnt
    temp = num

    while True :
        rst = ((temp % 10) * 10) + ((int(temp * 0.1) + (temp % 10)) % 10)
        temp = rst
        cnt += 1
        if rst == ori :
            break

ori = int(input().strip())
cnt = 0
getcnt(ori)

print(cnt)