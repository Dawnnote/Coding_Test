def solution(n):
    if n == 1:
        return 1

    binary = []
    while True:
        if n%3 == 0:
            binary.append(n%3)
            n = int(n/3)

        elif n%3 == 1:
            binary.append(n%3)
            n = int(n/3)

        elif n%3 == 2:
            binary.append(n%3)
            n = int(n/3)

        if n <= 2:
            binary.append(n)
            break

    binary.reverse()

    result = []
    for idx, i in enumerate(binary):
        if i == 0:
            continue
        result.append(i*3**idx)
        
    return sum(result)