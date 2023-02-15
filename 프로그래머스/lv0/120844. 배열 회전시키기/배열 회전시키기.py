def solution(numbers, direction):
    result = []
    if direction == "right":
        result.append(numbers[-1])
        result.extend(numbers[0:-1])
        
    elif direction == "left":
        result.extend(numbers[1:])
        result.append(numbers[0])
    
    return result