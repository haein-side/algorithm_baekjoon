n = list(map(int,input().split()))
s = list(map(int,input().split()))

i = 0

while True :
    if s[i] < n[1] : print(f'{s[i]} ',end="")
    i += 1
    if i >= n[0] : break