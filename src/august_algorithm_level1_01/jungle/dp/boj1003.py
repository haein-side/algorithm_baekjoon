# 내가 푼 풀이
# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n = int(input())
    
#     dp = [[0, 0] for _ in range(n+1)] # 0이 출력되는 횟수, 1이 출력되는 횟수
    
#     dp[0] = [1, 0]
    
#     if n >= 2:
#         dp[1] = [0, 1]
#         for i in range(2, n+1):
#             dp[i][0] = dp[i-1][0] + dp[i-2][0]
#             dp[i][1] = dp[i-1][1] + dp[i-2][1]
#         print(dp[n][0], dp[n][1])
#     elif n == 0:
#         print(dp[0][0], dp[0][1])
#     elif n == 1:
#         dp[1] = [0, 1] # 따로 안 해주면 index error 남! (0을 입력 받았을 경우 때문에)
#         print(dp[1][0], dp[1][1])

# 다른 방식의 풀이 - 인덱스 숫자에 해당되는 0의 호출 횟수(zero[n])와 1의 호출 횟수(one[n])
def fibo(n):
    zero = [1, 0]
    one = [0, 1]

    if n >= len(zero):
        for i in range(2, n+1):
            zero.append(zero[i-1] + zero[i-2]) # 리스트에 "append"해줘야 index error 안 남
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])

t = int(input())
for i in range(t):
    n = int(input().strip())
    fibo(n)