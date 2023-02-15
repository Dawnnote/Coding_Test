def solution(price):
    discount = {500000 : 0.8, 300000 : 0.9, 100000 : 0.95, 0 : 1}
    for result, discount_price in discount.items():
        if price >= result:
            return int(price * discount_price)