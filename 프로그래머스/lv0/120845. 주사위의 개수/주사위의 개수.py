def solution(box, n):
    result = 1
    for i in range(3):
        result *= int(box[i])//n
        
    return result