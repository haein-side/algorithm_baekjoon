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
    print(num[index], count, index)
    if count == k:
        arr.append(num[index])
        print(arr)
        remove += 1
        count = 1
    else:
        count += 1
        
    index += 1    
    if index >= 7:
        index -= index // 7 * 7

        

print(arr)
    
    
    