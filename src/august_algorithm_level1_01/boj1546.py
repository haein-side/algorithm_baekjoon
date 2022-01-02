N = int(input())
n = list(map(int,input().split()))
M = max(n)
sum = 0

for i in range(N):
    n[i] = n[i]/M*100
    sum += n[i]

print(sum/N)