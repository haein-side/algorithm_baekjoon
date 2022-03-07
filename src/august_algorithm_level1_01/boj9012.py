import sys

def sol(word):
    first = 0
    second = 0
    for i in range(len(word)):
        if word[i] == "(":
            first += 1
        elif word[i] == ")":
            second += 1
    if first == second:
        return "YES"
    else:
        return "NO"

n = int(sys.stdin.readline())

for i in range(n):
    word = sys.stdin.readline().strip()
    print(sol(word))