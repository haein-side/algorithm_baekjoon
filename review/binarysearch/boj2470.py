import sys

N = int(sys.stdin.readline())
W = sorted(list(map(int, sys.stdin.readline().split()))) # 오름차순으로 정렬

start = 0
end = N - 1
minValue = W[0] + W[N-1]
x = start
y = end

while start < end:
    sum = W[start] + W[end]
    
    if sum == 0:
        x = start
        y = end
        break
    
    if abs(minValue) > abs(sum):
        x = start
        y = end
        minValue = sum
   
    if sum > 0:
        end -= 1
    elif sum < 0:
        start += 1
    

print(W[x], W[y])
