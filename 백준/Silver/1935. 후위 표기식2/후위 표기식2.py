N = int(input())
operator = input()
num = [int(input()) for i in range(N)]

stack = []

for i in operator:
    if i.isalpha():                             # 문자 일때
        stack.append(num[ord(i)-ord('A')])      # ord는 문자를 유니코드 정수로 바꾸어준다
    else:                                       # 문자가 아닌 연산자를 기호를 만날 때
        op2 = stack.pop()                       # 해당 숫자(유니코드)가 담긴 stack에 pop을 해서 op2, op1, 변수에 담아준다
        op1 = stack.pop()

        if i == '*':
            stack.append(op1*op2)
        elif i == '+':
            stack.append(op1+op2)
        elif i == '/':
            stack.append(op1/op2)
        elif i == '-':
            stack.append(op1-op2)

print(f"{stack[0]:.2f}")
