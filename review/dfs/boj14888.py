import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
pl, mi, mul, na = map(int, input().split())

maxNum = -1e9
minNum = 1e9
def cal(depth, total, pl, mi, mul, na):
    global maxNum, minNum
    if depth == N-1:
        maxNum = max(maxNum, total)
        minNum = min(minNum, total)
        return
    
    if pl > 0:
        cal(depth+1, total + num[depth+1], pl-1, mi, mul, na)
    if mi > 0:
        cal(depth+1, total - num[depth+1], pl, mi-1, mul, na)
    if mul > 0:
        cal(depth+1, total * num[depth+1], pl, mi, mul-1, na)
    if na > 0:
        if total < 0:
            moc = (-total) // num[depth+1]
            total = -moc 
        else:
            total = total // num[depth+1]
        cal(depth+1, total, pl, mi, mul, na-1)



cal(0, num[0], pl, mi, mul, na)
print(maxNum)
print(minNum)