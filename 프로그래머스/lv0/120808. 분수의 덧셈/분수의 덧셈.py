import fractions
def solution(denum1, num1, denum2, num2):
    answer = []
    x = fractions.Fraction(denum1, num1)
    y = fractions.Fraction(denum2, num2)
    z = x + y

    answer.append(z.numerator)
    answer.append(z.denominator)

    return answer