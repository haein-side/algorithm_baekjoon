import sys
input = sys.stdin.readline

n = input().strip()
num = n.split('-') # ['55', '50+40']

for i in range(len(num)):
    tmp = map(int, num[i].split('+'))
    num[i] = sum(tmp)

res = num[0]
for i in range(1, len(num)):
    res -= num[i]

print(res)
    