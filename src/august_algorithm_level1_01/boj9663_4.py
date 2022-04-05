import sys

n = int(sys.stdin.readline())
mlist=[0]*n

def check(mlist, row):
    for i in range(row):
        if mlist[i] == mlist[row] or abs(mlist[row]-mlist[i]) == row - i:
            return False # 방문할 수 없는 경우이므로 False 주기
    return True

def search(mlist, row):
    count = 0
    if n == row:
        return 1
    
    for col in range(n):
        mlist[row] = col
        if check(mlist, row):
            count += search(mlist, row+1)
    
    return count

print(search(mlist, 0))