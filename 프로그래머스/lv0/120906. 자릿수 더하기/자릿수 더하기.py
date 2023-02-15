def solution(n):
    num = str(n)
    result = 0
    for i in range(len(num)):
        result += int(num[i])
    return result
