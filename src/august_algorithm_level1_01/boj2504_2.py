s = "(()[[]])([])" 
stack = []
tmp = 1
res = 0

for i in range(len(s)):
  if s[i] == '(':
    tmp *= 2
    stack.append(s[i])
  elif s[i] == '[':
    tmp *= 3
    stack.append(s[i])

  elif s[i] == ')':
    if not stack or stack[-1] == '[':
      res = 0 # 제대로 된 괄호 아닌 경우
      break
    if s[i-1] == '(':
      res += tmp # 짝을 찾았으므로 최종 결과에 더해줌
    tmp //= 2 # (( 열린 괄호가 2개 있는 경우 2가 곱해지는 건 1번이므로 짝이 만들어졌다면 2로 나눠줘야
    stack.pop() # pop도 까먹지 말고 꼭
  
  else: # n[i] == "]"
    if not stack or stack[-1] == '(':
      res = 0 # 제대로 된 괄호 아닌 경우
      break
    if s[i-1] == '[':
      res += tmp
    tmp //= 3
    stack.pop() # pop 까먹지 말기

if stack: # stack이 모두 pop되지 않아 비어있지 않은 경우 제대로 된 괄호가 아니므로 res = 0!
  res = 0
print(res)

# 참고 블로그 : https://dev-dain.tistory.com/149