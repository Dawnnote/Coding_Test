def solution(array):
    array.sort()
    if len(array) % 2 == 1:
        return array[int((len(array)-1)/2)]
