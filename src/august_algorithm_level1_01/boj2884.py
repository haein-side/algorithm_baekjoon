# time = [None] * 2

# time[0], time[1] = input().split()

# H = int(time[0])
# M = int(time[1])

H, M = map(int,input().split())

M = H*60 + M - 45

H = M // 60
if  H == -1 :
    H = 23
M = M % 60

print(f'{H} {M}')