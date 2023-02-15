def solution(polynomial):
    polynomial = polynomial.split(' + ')
    polynomial

    lis1 = []
    lis2 = []
    result = ''
    
    for i in polynomial:
        if 'x' in i:
            lis1.append(i)
        else:
            lis2.append(i)

    for i in range(len(lis1)):
        if lis1[i] in 'x':
            lis1[i] = 1

        elif 'x' in lis1[i]:
            lis1[i] = int(lis1[i].strip('x'))


    for i in range(len(lis2)):
        lis2[i] = int(lis2[i])


    if str(sum(lis2)) == '0':
        result = str(sum(lis1)) + 'x'
    
    elif sum(lis1) == 0:
        result = str(sum(lis2))
        
    elif sum(lis1) == 1:
        result = 'x' + ' + ' + str(sum(lis2))
        
    else:
        result = str(sum(lis1)) + 'x' + ' + ' + str(sum(lis2))

    if sum(lis1) == 1 and sum(lis2) == 0:
        result = 'x'

    
    return result