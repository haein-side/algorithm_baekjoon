lottos =[44,1,0,0,31,25]
win_nums=[31,10,45,1,6,19]

rank=[6,6,5,4,3,2,1]

cnt_0 = lottos.count(0)
print(cnt_0)

ans = 0
for x in win_nums:
    if x in lottos:
            ans += 1
print(rank[cnt_0 + ans],rank[ans])
