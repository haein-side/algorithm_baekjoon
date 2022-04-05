import sys

result = 0


def z(n, x, y): # 현재 위치 (x, y)
    global result
    if x == r and y == c: # 현재 위치와 목표 지점이 같을 때
        print(int(result))
        exit(0)

    if n == 1:
        result += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return
    z(n / 2, x, y)
    z(n / 2, x, y + n / 2)
    z(n / 2, x + n / 2, y)
    z(n / 2, x + n / 2, y + n / 2)


n, r, c = map(int, sys.stdin.readline().split(' ')) # 목표지점은 (r, c) r행 c열
z(2 ** n, 0, 0)