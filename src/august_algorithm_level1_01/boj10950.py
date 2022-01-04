n = int(input())
s = [None] * n

for i in range(n):
    s[i] = list(map(int,input().split()))
    
# print(s)

for i in range(n):
    print(s[i][0] + s[i][1])