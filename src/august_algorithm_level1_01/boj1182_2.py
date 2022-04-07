from sys import stdin
input = stdin.readline

N, S = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
cnt = 0

for i in range(N) :
        for k in range(N, i + 2, -1) :
            print(A[i:k])
            if sum(A[i:k]) == S :
                cnt += 1

print(cnt)

# 4 0
# -3 -2 3 2
# [-3, -2, 3, 2]
# [-3, -2, 3]
# [-2, 3, 2]
# 1 <= 3이 출력되어야!