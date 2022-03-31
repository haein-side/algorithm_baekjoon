import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

n = a * b * c
s = str(n)

dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in range(len(s)):
    if int(s[i]) in dic.keys():
        dic[int(s[i])] = dic.get(int(s[i])) + 1
        
for i in list(dic.values()):
    print(i)