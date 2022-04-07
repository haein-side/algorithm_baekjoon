import sys

n = int(sys.stdin.readline())
a = n
count = 0
tsum = 0

while True: # a와 n이 같지 않을 때까지만 반복
    sum = 0
    if n < 10:
        sum = n
    else:
        sum = int(str(n)[0]) + int(str(n)[1])
    
    if n < 10:
        tsum = str(n) + str(sum)
    else:
        tsum = str(n)[1] + str(sum)[len(str(sum))-1]
    
    count += 1
    
    n = int(tsum)
    
    if int(tsum) == a:
        break
    
print(count)