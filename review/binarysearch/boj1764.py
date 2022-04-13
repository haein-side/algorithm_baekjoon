import sys

N, M = map(int, sys.stdin.readline().split())
hear = {}
answer = []

for i in range(N):
    hear[sys.stdin.readline().strip()] = 1 

for i in range(M):
    a = sys.stdin.readline().strip()
    
    if a in hear.keys():
        answer.append(a)

print(len(answer))

answer = sorted(answer)
for i in answer:
    print(i)