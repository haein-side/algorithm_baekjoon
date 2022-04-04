import sys
import itertools

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
mlist = list(map(int, sys.stdin.readline().split()))
olist = ["+", "-", "*", "%"] # 따로 리스트 만들어주고 인덱스 번호 같게 해서 매칭시켜주기
plist = []

for i in range(len(mlist)):
    for j in range(mlist[i]):
        plist.append(olist[i])

perm = list(itertools.permutations(plist, len(plist)))

result = []
for i in range(len(perm)):
    r = nlist[0]
    for j in range(len(plist)):
        if perm[i][j] == "+":
            r += nlist[j+1]
        elif perm[i][j] == "-":
            r -= nlist[j+1]
        elif perm[i][j] == "*":
            r = r * nlist[j+1]
        elif perm[i][j] == "%":
            if r < 0:
                a = abs(r)//nlist[j+1]
                r = -a
            else:
                r = r//nlist[j+1]
    result.append(r)

print(max(result))
print(min(result))
