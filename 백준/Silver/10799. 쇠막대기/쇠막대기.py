bar = input()

stack = []
result = 0

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append('(')
        continue

    elif bar[i] == ')':
        if bar[i-1] == '(':
            stack.pop()
            result += len(stack)

        else:
            stack.pop()
            result += 1

print(result)