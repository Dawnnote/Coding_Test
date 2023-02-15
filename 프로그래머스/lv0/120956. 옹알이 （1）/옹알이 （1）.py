def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    lis = []
    result = 0

    for i in range(len(babbling)):
        for j in range(len(speak)):
            if speak[j] in babbling[i]:
                babbling[i] = babbling[i].replace(speak[j],'@')

    for i in range(len(babbling)):
        if babbling[i].replace('@','') == '':
            result += 1
    
    return result