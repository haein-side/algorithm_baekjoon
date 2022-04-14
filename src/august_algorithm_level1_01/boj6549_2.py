# 주형님 코드
from sys import stdin
from collections import deque
input = stdin.readline
# stack에서 pop을 해줄 때,
# 직전 인덱스 즉 i-1 에서, pop을 한 이후 남아있는, 즉 그 직전 인덱스 before를 참고해
# (i-1-before)*h를 해줘야 함. 만약 before가 없는 즉 stack이 빈 경우엔, 그냥 전체길이 i가 가로길이가 됨.
# 만약 for문 다 돌고나서 하는 경우엔
# (n-1-before)*h를 해주는 것임. 만약 before가 없는 즉 stack이 빈 경우엔, 그냥 전체길이 n이 가로길이가 됨.
while True:
    n, *case = list(map(int,input().split()))
    if n == 0:
        break
    stack = deque()
    area = [] # 넓이들을 저장하는 area
    for i in range(n):
        now = [i,case[i]]
        if not stack:
            stack.append(now)
        else:
            while stack[-1][-1] > now[-1]:
                idx, h = stack.pop()
                if not stack:
                    print(stack)
                    area.append(i*h)
                    break
                before = stack[-1][0]
                area.append((i-1-before) * h)
            stack.append(now)
    while stack:
        idx, h = stack.pop()
        if not stack:
            area.append(n*h)
            break
        before = stack[-1][0]
        area.append((n-1-before)*h)
    print(max(area))
            