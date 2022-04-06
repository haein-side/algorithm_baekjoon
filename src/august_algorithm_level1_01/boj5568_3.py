import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card = []
for i in range(n):
    card.append(sys.stdin.readline().strip())
result = []
    
def pick(card, depth, cur):
    global result

    if depth == k:
        # print(cur)
        result.append(cur)
        # result = list(set(result))
        return
    
    for i in range(n):
        pick(card, depth + 1, cur + card[i])
        # depth = 0
        cur = ''
    

pick(card, 0, '')

print(len(result))
print(result)