def solution(absolutes, signs):
    result = []
    
    for i in range(len(signs)):
        if signs[i] == True:
            result.append(absolutes[i])
        elif signs[i] == False:
            result.append(-(absolutes[i]))
            
    return sum(result)