def solution(price):
    discount = {500000 : 0.8, 300000 : 0.9, 100000 : 0.95, 0 : 1}
    for result, discount_price in discount.items():
        if price >= result:
            return int(price * discount_price)
        
#     if price >= 500000:
#         price *= 0.8
#     elif price >= 300000:
#         price *= 0.9
#     elif price >= 100000:
#         price *= 0.95
        
#     return int(price)