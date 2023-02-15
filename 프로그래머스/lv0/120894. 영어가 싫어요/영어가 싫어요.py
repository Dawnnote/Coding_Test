def solution(numbers):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, num in enumerate(number):
        numbers = numbers.replace(num, str(idx))
    
    return int(numbers)