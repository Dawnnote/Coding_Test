S = input()

result = ''
stack = ''
check = False

for i in S:
    if i == '<':
        check = True
        result += stack[::-1] + '<'
        stack = ''
        continue
    
    elif i == '>':
        check = False
        result += i
        continue

    elif i == ' ':
        result += stack[::-1] + ' '
        stack = ''
        continue
    
    if check:
        result += i
    else:
        stack += i

print(result+stack[::-1])