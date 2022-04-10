import sys
N = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(N-1, -1, -1):
    count = 0
    for j in range(i-1, -1, -1):
        if t[i] <= t[j]:
            result.append(str(j+1))
            count += 1
            break
    if count == 0:
        result.append("0")

print(" ".join(result[::-1]))
    
# print(result)