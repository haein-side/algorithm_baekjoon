import sys

def sol(a, b, c):
    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)
    
    maxnum = max(arr)
    arr.remove(maxnum)
    
    if maxnum*maxnum == arr[0]*arr[0] + arr[1]*arr[1]:
        return "right"
    else:
        return "wrong"
    
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    else:
        print(sol(a, b, c))

    
