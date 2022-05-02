# n = int(input())

# result = 1
# while n >= 1:
#     result *= n
#     n -= 1
    
# print(result)

n = int(input())

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

print(fac(n))