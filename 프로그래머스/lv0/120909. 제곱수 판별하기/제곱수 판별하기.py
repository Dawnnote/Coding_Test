def solution(n):
    result = n**0.5
    if int(result) == result:
        return 1
    else:
        return 2