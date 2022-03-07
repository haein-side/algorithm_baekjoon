import sys

def sol(word):
    comment = ""
    for i in range(len(word)):
        if word[i] == "(":
            comment = comment + "1"
        elif word[i] == ")":
            comment = comment + "0"
    while True:
        if comment.find("10"):
            comment.replace("10","")
        else:
            break
    if len(comment) > 0:
        return "NO"
    else:
        return "YES"


n = int(sys.stdin.readline())

for i in range(n):
    word = sys.stdin.readline().strip()
    print(sol(word))