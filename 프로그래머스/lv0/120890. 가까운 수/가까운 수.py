def solution(array, n):
    lis = []
    array.sort()
    for i in array:
        lis.append(abs(i-n))
    return array[lis.index(min(lis))]