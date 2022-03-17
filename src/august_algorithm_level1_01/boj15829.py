from sys import stdin
import math

L = int(stdin.readline())
word = stdin.readline().strip()
dic = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 
    'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
    'k':11, 'l':12, 'm':13, 'n':14,'o':15,
    'p':16,'q':17,'r':18, 's':19,'t':20,
    'u':21, 'v':22, 'w':23,'x':24,'y':25, 'z':26
}

result = 0
count = 0
for i in word:
    result += math.pow(31,count) * dic[i]
    count += 1

print(int(result % 1234567891))