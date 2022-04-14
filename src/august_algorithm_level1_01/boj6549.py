# 주형님 코드
# 기존에 짰던 코드
# 스택 두개 활용
from sys import stdin
from collections import deque
input = stdin.readline
while True:
    rectangles = list(map(int,input().split()))
    n = rectangles.pop(0)
    if n == 0:
        break
    left = [0]*n
    right = [n]*n
    stack = deque()
    # 이번엔 왼쪽에서 보면서 right 배열을 채워봄.
    for i in range(n):
        case = [i, rectangles[i]]
        if not stack:
            stack.append(case)
        else:
            while stack[-1][-1] > case[1]:
                right[stack.pop()[0]] = i
                if not stack:
                    break
            stack.append(case)
    stack.clear()
    # 이번엔 오른쪽에서 보면서 left 배열을 채워봄.
    for j in range(n-1, -1, -1):
        case = [j, rectangles[j]]
        if not stack:
            stack.append(case)
        else:
            while stack[-1][-1]>case[1]:
                left[stack.pop()[0]] = j+1
                if not stack:
                    break
            stack.append(case)
    
    ans = 0
    for k in range(n):
        area = (right[k]-left[k])*rectangles[k]
        ans = max(ans, area)
    print(ans)
