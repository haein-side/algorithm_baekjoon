# from itertools import permutations

# 메모리 초과
# n = int(input())

# dp = [0] * (n+1)

# maxzero = n//2

# if n % 2 == 0:
#     tmp = 1 + 1
# else:
#     tmp = maxzero + 1 + 1 # 가장 0 이 많을 때 + 0이 한 개도 없을 때

# mid = []
# for i in range(1, maxzero):
#     set = []
#     for j in range(i):
#         set.append(0)
#     for k in range(n - 2*i):
#         set.append(1)
#     tmp += len(list(permutations(set))) // 2

# dp[n] = tmp
# dp[1] = 1
# dp[2] = 2

# print(dp[n])


# # dp 활용 (피보나치와 같은 규칙) - 인덱스 에러남
# n = int(input())
# dp = [0] * (n+1)
# dp[1] = 1
# dp[2] = 2

# if n >= 3:
#     for i in range(3, n+1):
#         dp[i] = (dp[i-2] + dp[i-1]) % 15746

# print(dp[n])

# dp 활용 (인덱스 에러 수정) - n에 1이 들어왔을 시, 2가 없으므로 인덱스 에러
# n = int(input())
# dp = [0] * (n+1)
# if n == 1:
#     dp[1] = 1
# else:
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, n+1):
#         dp[i] = (dp[i-2] + dp[i-1]) % 15746
        
# print(dp[n])

# dp 활용 (리스트 대신 변수 활용)
n = int(input())
if n == 1:
    print(1)
else:
    res = 0
    n1 = 1
    n2 = 2
    if n == 2:
        print(2)
    else:
        for i in range(3, n+1):
            res = (n1 + n2) % 15746
            n1, n2 = n2, res
        print(res)