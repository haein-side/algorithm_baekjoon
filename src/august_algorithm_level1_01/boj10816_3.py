from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
target = list(map(int, stdin.readline().split()))

count = dict()
for i in data:
    try: count[i] += 1
    except: count[i] = 1
    
for i in target:
    try: print(str(count[i]), end = " ")
    except: print("0", end = " ")
