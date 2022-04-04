# 잘 이해가 안 가는 풀이
import sys
from itertools import permutations

n,cost=int(input()),0 # 도시의 수 n개
city,result=[],1000000*n
order=[i for i in range(n)] # 도시 순서를 나타내기 위해 [0,1,2,3] 이런 식으로 배열 만들어줌

for i in range(n):
    city.append(list(map(int,sys.stdin.readline().split())))

print(city)

for i in permutations(order,n): # 도시 i
    print(i, i[-1], i[0], city[i[-1]][i[0]])
    if(city[i[-1]][i[0]]!=0):
        for j in range(n-1):
            print(j, city[i[j]][i[j+1]])
            if(city[i[j]][i[j+1]]==0):
                cost=0
                break
            cost+=city[i[j]][i[j+1]]
        print("======")
        if(cost!=0):
            cost+=city[i[-1]][i[0]]
            result=min(cost,result)
    cost=0
print(result)