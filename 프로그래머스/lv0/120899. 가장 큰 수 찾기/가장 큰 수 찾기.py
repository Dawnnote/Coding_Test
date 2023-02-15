def solution(array):
    result = []
    result.extend([max(array), array.index(max(array))])
    return result
    