import sys
nn = int(sys.stdin.readline())
kk = int(sys.stdin.readline())
arr = []

for i in range(nn):
    arr.append(sys.stdin.readline().strip())
    
string = []
result = set()


def splice(arr, n): # 본인은 제외한 것을 리턴해주는 함수
    return arr[0:n] + arr[n+1:len(arr)] # arr은 안 건드리고 본인은 제외한 리스트를 새로 만들어서 리턴해주는 것

def setCards(arr, k):
    global string
    n = len(arr)  
    
    if k <= 0 :
        result.add(''.join(string))
        return   

    for i in range(n):  
        string.append(arr[i])
        setCards(splice(arr,i), k-1) # 방금 전에 뽑은 것을 리스트에서 제외하고 그 중에서 k-1개 뽑아줘야 함
        string.pop() # string을 pop해줘야 복구가 됨 (재귀 끝나고 복구)

setCards(arr, kk)
print(len(result))
print(result)