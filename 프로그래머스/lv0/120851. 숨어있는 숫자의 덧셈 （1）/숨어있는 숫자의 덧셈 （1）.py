def solution(my_string):
    result = 0
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            result += int(my_string[i])
    return result