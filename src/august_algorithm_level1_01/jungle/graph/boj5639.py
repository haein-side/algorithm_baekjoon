import sys

# 입력받을 원소 리스트
num_list = []
while True:
    try: # 일단 시도는 할 코드
        num = int(sys.stdin.readline())
        num_list.append(num)
    except: # try에서 오류 발생 시 실행할 코드
        break

# 재귀로 작성은 너무 어려움..
# def sol(root, left, right):

first = num_list[0]
left = [] # 좌측 자식 노드
right = [] # 우측 자식 노드

for i in range(1, len(num_list)):
    if first > num_list[i]:
        left.append(num_list[i])
    else:
        right.append(num_list[i])

print(left)
print(right)