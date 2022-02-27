x, y = map(int, input().split())
a, b = x, y
small = 0

if x <= y:
    small = x
else:
    small = y
arr = []
n = 2
while n <= small:
    if x % n == 0 and y % n == 0:
        x = x // n
        y = y // n
        arr.append(n)
        n = 2
    else:
        n += 1

if not arr == 0 :
    arr.append(1)
    
answer1 = 1
for i in arr:
    answer1 = answer1 * i

print(answer1)
print(a*b//answer1)