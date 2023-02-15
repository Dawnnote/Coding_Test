def solution(n, numlist):
    result = []
    for i in range(len(numlist)):
        if numlist[i] % n == 0:
            result.append(numlist[i])
    return result
        