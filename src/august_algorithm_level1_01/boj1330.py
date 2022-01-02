# 두 수 비교하기 - 1
n=[None] * 2
n[0], n[1] = input().split()

n[0] = int(n[0])
n[1] = int(n[1])

if n[0] > n[1] :
    print('>')
if n[0] == n[1] :
    print('==')
if n[0] < n[1] :
    print('<')

# 두 수 비교하기 - 2
n = list(map(int, input().split()))

if n[0] > n[1] :
    print('>')
elif n[0] < n[1] :
    print('<')
else :
    print('==')