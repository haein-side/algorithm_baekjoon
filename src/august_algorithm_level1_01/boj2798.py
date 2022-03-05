import sys
import itertools

N, M = map(int, input().split())
arr = []

num = list(map(int, sys.stdin.readline().split()))

result = list(itertools.combinations(sorted(num),3))

for i in range(len(result)):
    if M >= sum(result[i]):
        arr.append(sum(result[i]))

print(max(arr))