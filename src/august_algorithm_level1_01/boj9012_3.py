import sys

def sol(word):
    answer = "NO"
    sum = 0
    for i in range(len(word)):
        if word[i] == "(":
            sum += 1
        elif word[i] == ")":
            sum -= 1
        if sum == -1:
            return answer
            break
    if sum == 0:
        answer = "YES"
    return answer

n = int(sys.stdin.readline())

for i in range(n):
    word = sys.stdin.readline().strip()
    print(sol(word))