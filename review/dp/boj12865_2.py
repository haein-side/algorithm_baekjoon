import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stuff = [[0,0]]
for _ in range(n):
    stuff.append(list(map(int, input().split())))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)] # k가 7일 때 dp는 0 1 2 3 4 5 6 7 되도록 k+1까지 만들어줌
# dp[i][j]는 stuff의 i번째 무게를 넣었을 때 만들어지는 총합이 j무게일 때의 최대 가치

for i in range(1, len(stuff)): # 0부터 초기화를 해서 7까지 입력을 해줬으므로 len
    for j in range(1, len(dp[i])): # 2차원 배열로서 모두 0으로 초기화되어 있으므로 경우의 수 다 고려해줘야
                      # 처음에 len(dp)로 했다가 행의 갯수만 세어져서 열의 갯수로 수정함
                      # 더 좋은 방법: len(stuff) -> n+1, len(dp[i]) -> k+1로 수정하기
        weight = stuff[i][0]
        value = stuff[i][1]
        if weight > j: 
        # 나보다 총합이 큰 경우 -> 채워줄 수 없으므로 바로 위의 행 값 가져옴 (나 안 넣고 동일 무게 만드는 데 최대 가치)
            dp[i][j] = dp[i-1][j]
        else: 
        # 나보다 총합이 이하인 경우: 나를 안 넣었을 때 vs. 나를 넣었을 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value) # i가 행으로 i-1 아직 내꺼 안 넣었을 때 j는 무게

print(dp[n][k])
        
            
