S = input()

for i in S:
    if i.islower():
        if ord('z') < (ord(i)+13):
            print(chr((ord(i)+13)-ord('z')+ord('a')-1), end="")
        else:
            print(chr(ord(i)+13), end="")
    
    elif i.isupper():
        if ord('Z') < (ord(i)+13):
            print(chr((ord(i)+13)-ord('Z')+ord('A')-1), end="")
        else:
            print(chr(ord(i)+13), end="")
    else:
        print(i, end='')