import sys
n = int(sys.stdin.readline())
s = str(n)

if n <= 99:
    print(n)
else:
    a = 0
    
    for i in range(100, n+1):
        c = int(str(i)[0])-int(str(i)[1])
        for j in range(1, len(str(i))-1):
            if int(str(i)[j]) - int(str(i)[j+1]) != c:
                # print(int(str(i)[j]), int(str(i)[j+1]))
                break
        else:
            a += 1
    print(a + 99)