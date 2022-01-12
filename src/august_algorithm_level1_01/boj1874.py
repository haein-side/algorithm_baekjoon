n = int(input())
A = []
B = []
S = [1]
ans = ""
for i in range(n) :
  A.append(int(input()))
  B.append(i+1)

print('+')

for i in range(n-1):
  if A.index(B[i]) < A.index(B[i+1]):
    print('+')
    S.append(B[i])
  else :
    print('-')
    if B[i] in S:
      S.remove(B[i])
      ans += " " + str(B[i])
      print(ans)

print(ans)
print(B)

# https://assaeunji.github.io/python/2020-05-04-bj1874/
# https://pacific-ocean.tistory.com/231
# https://hongcoding.tistory.com/39