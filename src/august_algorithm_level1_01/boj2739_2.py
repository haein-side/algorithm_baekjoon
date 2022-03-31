import sys

n = int(sys.stdin.readline())

for i in range(9):
    print(n,"*",i+1,"=",n*(i+1))