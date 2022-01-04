alpha = [None] * 26

def listAlphabet():
    return [chr(i) for i in range(ord('a'),ord('z')+1)]
print(listAlphabet())

# for i in range(26) :
#     chr(i) for i in range(ord('a'),ord('z')+1)
# print(alpha)