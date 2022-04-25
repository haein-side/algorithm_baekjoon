import sys
input = sys.stdin.readline

n = int(input())
pibo = [0, 1]

for i in range(n):
    pibo.append((pibo[i] + pibo[i+1])%15746)

print(pibo[-1])