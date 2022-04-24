import sys
input = sys.stdin.readline

string = input().strip()
string = string.split('-') # ['55', '50+40']
mid = []
for i in string:
    tmp = []
    tmp = i.split('+')
    tmp = list(map(int, tmp)) # 리스트의 문자열 원소를 int형으로 바꿔줌
    mid.append(sum(tmp))
    
res = mid[0]
for j in range(1, len(mid)):
    res -= mid[j]
    
print(res)