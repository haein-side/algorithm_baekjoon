# 동전 2 https://www.acmicpc.net/problem/2294와 유사
# 동전 2는 BFS와 다이나믹 프로그래밍이 결합된 문제
# 동전은 '모든' 방법의 수를 출력하는 것
# 동전 2는 사용한 동전의 '최소 개수'를 출력하는 것 (그래서 heap을 사용)

from collections import deque
import sys
input = sys.stdin.readline

T = int(sys.stdin.readline())

for i in range(T):
    tnum = int(input()) # 동전 종류
   
    coins = list(map(int, input().split()))

    k = int(input())
    
    dp = [0] * (k+1)
    dp[0] = 1 # 동전이 1개만 필요할 경우를 고려하기 위해
    for i in coins: # 동전 i로
        for j in range(i, k+1): # 동전의 합을 j로 만들어줄 때 (i이상의 합을 만들어줄 수 있음)
            dp[j] += dp[j-i]
    
    print(dp[k])
    