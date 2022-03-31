import sys

nlist = []

for i in range(9):
    nlist.append(int(sys.stdin.readline()))
    
print(max(nlist))
print(nlist.index(max(nlist))+1)