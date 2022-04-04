import sys
nn = int(sys.stdin.readline())
kk = int(sys.stdin.readline())
arr = []

for i in range(nn):
    arr.append(sys.stdin.readline().strip())
    
string = []
result = set()


def splice(arr, n):
    return arr[0:n] + arr[n+1:len(arr)]

def setCards(arr, k):
    global string
    n = len(arr)  
    
    if k <= 0 :
        result.add(''.join(string))
        return   

    for i in range(n):  
        string.append(arr[i])
        setCards(splice(arr,i), k-1)