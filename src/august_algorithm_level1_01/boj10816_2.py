import sys

n = int(sys.stdin.readline())
card = list(sys.stdin.readline().split())

m = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())
answer = []

def binary(target, data):
    start = 0
    end = len(data)-1
    count = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target :
            count += 1
        elif data[mid] < target :
            start = mid + 1
        elif data[mid] > target :
            end = mid - 1
            
    return count


for i in arr:
    answer.append(binary(i, card.sort()))

print(answer)