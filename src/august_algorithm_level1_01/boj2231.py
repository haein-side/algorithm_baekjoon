import sys

M = int(sys.stdin.readline())
# M = int(input())

# print(len(str(M))) # 각 자릿수 구하기
# print(M // pow(10, len(str(M))-1))
# print(M- (M // pow(10, len(str(M))-1)) * 100// pow(10, len(str(M))-2))
answer = 0

for i in range(1, M+1):
    num = str(i)
    numlist = []
    for j in range(len(num)):
        numlist.append(int(num[j]))
        # print(numlist)
        # print(j)
    if i + sum(numlist) == M :
        answer = i
        break

print(answer)
    