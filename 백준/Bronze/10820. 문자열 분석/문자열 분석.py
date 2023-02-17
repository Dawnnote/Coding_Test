while True:
    try:
        S = input()

        result = [0, 0, 0, 0]
        for i in S:
            if i.islower():
                result[0] += 1
            elif i.isupper():
                result[1] += 1
            elif i.isdigit():
                result[2] += 1
            elif i == ' ':
                result[3] += 1

        print(" ".join(map(str, result)))
        
    except:
        break