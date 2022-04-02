n = int(input())
def m(n):
    if n == 1:
        return 1 # 원반이 1개 남았을 때는 한 번만 옮기면 되므로 1을 리턴해줌!!
    return 2 * m(n-1) + 1
print(m(n))