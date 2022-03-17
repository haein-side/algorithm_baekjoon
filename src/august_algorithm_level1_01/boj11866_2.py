from sys import stdin

n, k = map(int, stdin.readline().split())
num = list()

for i in range(n):
    num.append(i+1)

arr = list()
index = 0
count = 1
remove = 0

while remove <= n:
    print(num)
    if count == k:
        arr.append(num.pop(index))
        remove += 1
        count = 1
    else:
        count += 1
        index += 1    
        if index >= len(num)-1:
            index = 0

        

print(arr)
     
    
    