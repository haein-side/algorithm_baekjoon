import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(N)]
arr = arr[::-1]
cnt = 1
stack = [arr[0]]
for i in range(N):
    if arr[i] > stack[-1]:
        cnt += 1
        stack.pop()
        stack.append(arr[i])
        
print(cnt)