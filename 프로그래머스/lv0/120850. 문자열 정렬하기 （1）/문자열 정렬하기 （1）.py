def solution(my_string):
    result = []
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            result.append(int(my_string[i]))
            result.sort()
    return result
            
            