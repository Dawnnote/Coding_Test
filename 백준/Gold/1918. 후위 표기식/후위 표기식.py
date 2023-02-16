operator = input()

stack = []
result = ""

for op in operator:
    if op.isalpha():
        result += op

    elif op == "(":
        stack.append(op)

    elif op == '*' or op =='/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(op)

    elif op == '+' or op =='-':
        while stack and stack[-1] != "(":
            result += stack.pop()
        stack.append(op)

    elif op == ")":
        while stack and stack[-1] != "(":
            result += stack.pop()
        stack.pop()

while stack:
    result += stack.pop()
    
print(result)