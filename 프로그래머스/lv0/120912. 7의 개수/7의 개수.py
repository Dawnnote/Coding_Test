def solution(array):
    result = 0
    
    for i in array:
        result += str(i).count('7')
        
    return result