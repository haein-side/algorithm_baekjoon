N, K = map(int, input().split())
queue = list(range(1, N + 1))       # 1부터 N까지 있는 리스트

tmp = []        # 팝한 원소 넣을 리스트
idx = K - 1     # 순차적으로 도는 인덱스
# 빌 때까지 반복
while queue:
    if idx >= len(queue):   # 인덱스가 넘어가면 나머지로 바꿔줌
        print(idx)
        idx %= len(queue)
    else:   # 인덱스가 범위 내이면 해당 번째 원소 꺼내서 넣고 인덱스 다시 올림
        tmp.append(str(queue.pop(idx)))
        idx += K - 1

result = f'<{", ".join(tmp)}>'
print(result)