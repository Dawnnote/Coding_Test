def solution(quiz):
    
    result = []
    a = 0
    
    for i in range(len(quiz)):
        q = quiz[i].split()
        print(q)
        if q[1] == '-':
            a = int(q[0]) - int(q[2])
            if a == int(q[-1]):
                result.append('O')
            else:
                result.append('X')

        if q[1] == '+':
            a = int(q[0]) + int(q[2])
            if a == int(q[-1]):
                result.append('O')
            else:
                result.append('X')
                
    return result