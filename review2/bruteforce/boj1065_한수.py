import sys
input = sys.stdin.readline

n = int(input())
s = str(n)

if n <= 99:
    print(n)
else:
    count = 0
    for i in range(100, n+1):
        c = int(str(i)[0])-int(str(i)[1])
        for j in range(1, len(str(i))-1):
            if int(str(i)[j])- int(str(i)[j+1]) != c:
                break
        else:
            count += 1
    
    print(count+99)