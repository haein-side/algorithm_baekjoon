# n = int(input())
# A = []
# B = []
# S = [1]
# ans = ""
# for i in range(n) :
#   A.append(int(input()))
#   B.append(i+1)

# print('+')

# for i in range(n-1):
#   if A.index(B[i]) < A.index(B[i+1]):
#     print('+')
#     S.append(B[i])
#   else :
#     print('-')
#     if B[i] in S:
#       S.remove(B[i])
#       ans += " " + str(B[i])
#       print(ans)

# print(ans)
# print(B)

# # https://assaeunji.github.io/python/2020-05-04-bj1874/
# # https://pacific-ocean.tistory.com/231
# # https://hongcoding.tistory.com/39


# 풀었으나 시간초과가 난 풀이 (모든 조건들을 고려하여 머리 빠지게 풂 ㅎㅎ)

n = int(input())
s = []
b = []
for i in range(n):
    s.append(int(input()))
    b.append(i+1)

a = []
pop = len(s)
j = 0
answer = []

for i in range(n):
    a.append(b[i])
    # print('+')
    answer.append(1)
    
    while pop >= 1 and len(a) > 0:
        if a[len(a)-1] == s[j]:
            # print('-')
            answer.append(0)
            a.remove(a[len(a)-1])
            j += 1
            pop -= 1
        else:
            break

if pop != 0 :
    print('NO')
else :
    for i in answer:
        if i == 1:
            print('+')
        else :
            print('-')