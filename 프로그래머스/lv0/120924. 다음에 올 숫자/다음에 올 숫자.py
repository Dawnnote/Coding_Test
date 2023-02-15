def solution(common):
    result = 0
    if common[1] - common[0] == common[2] - common[1]:
        result = common[-1] + (common[1] - common[0])
    else:
        result = common[-1] * int(common[1]/common[0])

    return result