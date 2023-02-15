def solution(n):
    result = []
    for i in list(range(1, n+1)):
        if n % i == 0:
            result.append(i)
    return sorted(result)