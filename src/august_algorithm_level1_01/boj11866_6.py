import sys

N, K = map(int, sys.stdin.readline().split())
queue = list(range(1,N+1))

tmp = []
idx = K - 1

while queue:
    if idx >= len(queue):
        idx %= len(queue)
    else:
        tmp.append(str(queue.pop(idx)))
        idx += K - 1
    
result = f'<{", ".join(tmp)}>'

print(result)