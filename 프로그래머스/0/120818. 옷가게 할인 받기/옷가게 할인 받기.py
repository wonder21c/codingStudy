import math
def solution(price):
    answer = 0
    if 100000 <= price < 300000:
        answer = price - (price * 0.05)
    elif 300000 <= price < 500000 : 
        answer = price - (price * 0.1)
    elif price >= 500000:
        answer = price - (price * 0.2)
    else:
        answer = price
    return math.floor(answer)




def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
