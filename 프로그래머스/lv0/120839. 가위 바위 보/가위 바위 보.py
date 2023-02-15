def solution(rsp):
    result = []
    for i in range(len(rsp)):
        if rsp[i] == '2':
            result.append('0')
        elif rsp[i] == '0':
            result.append('5')
        else:
            result.append('2')
    return ''.join(result)