n = int(input())
cities = []

ways = [True]*n
now = 0
ways[now] = False

sums = []
sum = 0

for _ in range(n):
    cities.append(list((map(int, input().split()))))

# path = [now]

def travel(cities, now, sum):
    global ways    
    global sums
    
    c = ways.count(False)
    if c == n :
        if cities[now][0] : 
            sum += cities[now][0]
            sums.append(sum)
        # print(path, sum)
    
    for i in range(n):
        if not ways[i] : continue
        if cities[now][i] == 0 : continue
        
        t = cities[now][i]
        sum += t        
        pre = now
        now = i        
        ways[i] = False        
        # path.append(i)  
        travel(cities, now, sum)
        # path.pop()
        sum -= t
        now = pre
        ways[i] = True 
        
travel(cities, now, sum)
print(min(sums))