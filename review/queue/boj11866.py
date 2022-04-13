import sys

N, K = map(int, sys.stdin.readline().split())
que = list(range(1, N+1))
idx = K - 1
tmp = [] # 팝한 원소를 넣을 배열

while que :
    if idx >= len(que):
        idx %= len(que)
        # len(que)를 초과했으므로 idx를 큐의 길이로 나눠야 그 다음에 나머지 인덱스가 들어갈 수 있음

    tmp.append(str(que.pop(idx)))
    idx += K - 1

result = f'<{", ".join(tmp)}>'
print(result)