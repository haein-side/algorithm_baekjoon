n= []
while True :
    a = input()
    if a == '0' :
        break
    n.append(a)

for i in range(len(n)) :
    count = 0
    for j in range(len(n[i])//2):
        if n[i][j] == n[i][len(n[i])-j-1] :
            count += 1
    
    if count == len(n[i])//2 :
        print('yes')
    else :
        print('no')