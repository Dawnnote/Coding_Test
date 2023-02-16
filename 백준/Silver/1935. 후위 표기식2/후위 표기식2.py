N = int(input())
operator = input()
num = [int(input()) for i in range(N)]

stack = []

for i in operator:
    if i.isalpha():
        stack.append(num[ord(i)-ord('A')])
    else:
        op2 = stack.pop()
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
