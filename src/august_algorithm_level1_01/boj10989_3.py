import sys

n = int(sys.stdin.readline())

dict = {}
for i in range(10001):
    dict[i] = 0

for i in range(n):
    a = int(sys.stdin.readline())
    dict[a] += 1

for i in range(10001):
    if dict.get(i) > 0: # key가 없으면 None을 반환해줌! 처음에 없는 값을 대소비교하려고 해서 되지 않았음
        for j in range(dict.get(i)):
                print(i)
    
