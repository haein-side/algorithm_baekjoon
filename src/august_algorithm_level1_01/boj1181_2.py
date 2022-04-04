import sys

nlist = dict()

for i in range(51):
    nlist[i] = []

n = int(sys.stdin.readline())

for i in range(n):
    w = sys.stdin.readline().strip()
    nlist[len(w)] = nlist.get(len(w)) + [w]

print(nlist)  
  
for i in range(51):
    if len(nlist.get(i)) > 0:
        nlist[i] = set(nlist[i]) # 중복제거
        nlist[i] = sorted(nlist[i]) # 사전 순으로 정렬 // dict.get(key)가 아니라 nlist[i]를 통째로 sorted()해줘야 함!

for i in range(51):
    if len(nlist.get(i)) > 0:
        for j in range(len(nlist.get(i))):
            print(nlist.get(i)[j])