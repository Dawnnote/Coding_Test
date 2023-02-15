def solution(age):
    ag = f'{age}'
    code = 'abcdefghij'
    result = ''
    
    for i in ag:
        result += code[int(i)]
        
    return result
        