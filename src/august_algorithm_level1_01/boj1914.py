n = int(input())
c = 0
a = ''
def move(no, x, y):
    global c
    global a
    if no > 1:
        move(no-1, x, 6-x-y)
    if n <= 20:
        a = a + str(x) + " " + str(y) + '\n'
        c += 1
    
    if no > 1:
        move(no-1, 6-x-y, y)
        
move(n, 1, 3)
print(c)
print(a)