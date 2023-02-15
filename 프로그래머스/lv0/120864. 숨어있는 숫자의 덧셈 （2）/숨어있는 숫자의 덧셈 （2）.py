import re

def solution(my_string):
    lis = re.findall('\d+', my_string)
    result = 0
    
    for i in range(len(lis)):
        result += int(lis[i])
        
    return result