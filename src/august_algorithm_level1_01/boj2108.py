from collections import Counter
import sys

N = int(sys.stdin.readline())
num = []

# TypeError: 'int' object is not iterable
# 정수 자체는 반복할 수 없음
# for 변수 in 리스트(또는 튜플, 문자열):

for i in range(N):
    num.append(int(sys.stdin.readline()))

# 산술평균
# 소수 첫째 자리에서 반올림 round(숫자)
print(round(sum(num) / N))

# 중앙값
sortedlist = sorted(num)
print(sortedlist[(N-1)//2])

# 최빈값
cnt = Counter(num) # 각 데이터가 등장한 횟수를 딕셔너리 형식으로 보여줌 Counter({1: 2, 3: 1, 5: 1, 2: 1})
# print(cnt)
mode = cnt.most_common() # 등장 횟수만 내림차순으로 정리하여 보여줌 [(3, 2), (1, 2), (5, 1)]
# print(mode)
count = 0

# [(1, 1), (3, 1), (8, 1), (-2, 1), (2, 1)]
# [(-1, 2), (-2, 2), (-3, 1)]
# [(-2, 2), (-1, 2), (-3, 1)]

for i in range(len(mode)):
    if mode[0][1] == mode[i][1]:
        count += 1
modenum = []
if count >= 2:
    for i in range(count):
        modenum.append(mode[i][0])
    modenum = sorted(modenum) # 오름차순 정렬 [-2, 1, 2, 3, 8]
    print(modenum[1])
else:
    print(mode[0][0])



# 범위
print(sortedlist[N-1]- sortedlist[0])
    