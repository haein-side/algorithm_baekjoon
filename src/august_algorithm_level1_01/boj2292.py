import sys

M = int(sys.stdin.readline())

if M == 1:
    print(1)
else:
    i = 2
    cur = 0
    while True:
        if M < i :
            break
        else:
            cur += 1
            i = i + 6 * cur
    x = (i - 2) // 6
    j = 0
    while True:
        j += 1
        if j * (j+1) // 2 == x:
            break
    
    print(2+j-1)
        