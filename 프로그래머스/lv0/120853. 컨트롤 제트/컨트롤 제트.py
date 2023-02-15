def solution(s):
    result = 0
    s = s.split(' ')
    lis = []
    
    for i in range(len(s)):
        lis.append(s[i])
        if s[i] in 'Z':
            lis.remove(s[i-1])
            lis.remove('Z')

    for i in lis:
        result += int(i)
        
    return result