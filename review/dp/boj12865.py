import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stuff = []
for _ in range(n):
    stuff.append(list(map(int, input().split())))
dp = [0 for _ in range(k+1)] # k가 7일 때 dp는 0 1 2 3 4 5 6 7 되도록 k+1까지 만들어줌

stuff.sort()

for weight, value in stuff:
    # 뒤에서부터 채워야 짐이 여러번 들어가지 않음!
    # 앞에서부터 채우면 짐이 여러번 중복됨!
    for j in range(len(dp)-1, -1, -1): # dp의 인덱스를 모두 가져올 수 있음 (인덱스가 곧 무게)
        if j >= weight: # 무게의 총합보다 현재 무게가 이하일 때만 만들어줄 수 있음
            dp[j] = max(dp[j], dp[j-weight] + value)
print(dp[-1])