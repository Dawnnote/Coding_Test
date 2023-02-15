def solution(hp):
    result = 0

    result += hp//5
    hp -= (hp//5)*5

    result += hp//3
    hp -= (hp//3)*3

    result += hp//1
        
    return result