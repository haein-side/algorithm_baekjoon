N = int(input())

first = N // 5 + 1
second = 0
answer = -1

while first >= 0:
    sum = (5*first) + (3*second)
    if N == sum:
        answer = first + second
        break
    elif N < sum:
        first -= 1
    elif N > sum:
        second += 1

print(answer)