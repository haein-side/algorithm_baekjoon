from sys import stdin

L = int(stdin.readline())
word = stdin.readline().strip()
M = 1234567891

result = 0
for i in range(len(word)):
    num =  ord(word[i])-96
    result += 31**i * num
print(result % M)