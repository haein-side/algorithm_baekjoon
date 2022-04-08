import sys
n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))

def bsearch(w):
    w.sort()
    left = 0
    right = len(w) - 1
    al = 0
    ar = 0
    tmp = 999999
    while left <= right:
        if w[left] + w[right] == 0:
            al = left
            ar = right
            break
        if w[left] + w[right] > 0:
            right -= 1
        if w[left] + w[right] < 0:
            left += 1
        if tmp > abs(w[left] + w[right]):
            tmp = abs(w[left] + w[right])
            al = left
            ar = right
    return w[al], w[ar]

print(bsearch(w))