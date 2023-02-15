def solution(phone_number):
    return phone_number.replace(phone_number[:-4], '*'*len(phone_number[:-4]))