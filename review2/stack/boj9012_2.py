import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = input().strip()
    sum = 0
    for j in num:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
            if sum < 0:
                print("NO")
                break
    if sum > 0 :
        print("NO")
    elif sum == 0:
        print("YES")