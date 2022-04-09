import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
m = m[::-1]

count = 1
max = m[0]

for i in range(1, len(m)):
    if max < m[i]:
        count += 1
        max = m[i]

print(count)