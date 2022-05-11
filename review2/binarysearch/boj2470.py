import sys
input = sys.stdin.readline

n = int(input())
water = sorted(list(map(int, input().split())))

def bsearch():
    start = 0
    end = n-1
    first = 0
    second = 0
    minhap = float('inf')
    while start < end:
        hap = water[start] + water[end]
        if minhap >= abs(hap):
            minhap = abs(hap)
            first = water[start]
            second = water[end]
        if hap < 0:
            start += 1
        elif hap > 0:
            end -= 1
        else: # hap == 0
            first = water[start]
            second = water[end]
            break
    print(first, second)


bsearch()