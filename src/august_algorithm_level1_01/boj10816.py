import sys

n = int(sys.stdin.readline())
card = list(sys.stdin.readline().split())

m = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())

answer = ""

for i in range(len(arr)):
    answer = answer + str(card.count(arr[i])) + " "

print(answer.strip())