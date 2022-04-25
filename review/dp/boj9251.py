import sys
x = [0] + list(input())
y = [0] + list(input())

lcs = [[0 for _ in range(len(y))] for _ in range(len(x))]

for i in range(1, len(x)):
    for j in range(1, len(y)):
        # print(x[i], y[j])
        if x[i] == y[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            
print(lcs[len(x)-1][len(y)-1])