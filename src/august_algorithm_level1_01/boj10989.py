from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline()))

def quick_sort(arr):
    if len(arr) == 0:
        return arr
    
    pivot = arr[0]
    small_list = []
    equal_list = []
    big_list= []
    
    for i in range(arr):
        if pivot < arr[i]:
            big_list.append(arr[i])
        elif pivot > arr[i]:
            small_list.append(arr[i])
        else:
            equal_list.append(arr[i])
    
    result = quick_sort(small_list) + equal_list + quick_sort(big_list)
    
    return result

result = quick_sort(arr)    

for j in result:
    print(j)
