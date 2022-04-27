import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] # 첫번째 stairs는 쓰지 않음!

for _ in range(n):
    stairs.append(int(input()))
    
dp = [0 for _ in range(n+1)] # dp의 0의 개수를 n+1로 초기화 -> 첫번째 dp는 쓰지 않음!

if n == 1:
    print(stairs[1])
else:
    # dp[0]은 쓰지 않음!
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    
    for i in range(3, n+1):
        dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])

    print(dp[-1]) # 마지막 도착점에 도달하면 총 점수를 출력하기 위해 dp[-1]을 출력
    