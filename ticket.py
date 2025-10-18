import random

def get_numbers_tickets(min, max, quantity):
    if min >= max:
        print("Помилка: мінімальне число має бути менше за максимальне.")
        return []
    if quantity > (max - min + 1):
        print("Помилка: кількість чисел більша, ніж доступний діапазон.")
        return []
    if quantity <= 0:
        print("Помилка: кількість чисел повинна бути більшою за нуль.")
        return []
    
    return random.sample(range(min, max + 1), quantity)

lottery_numbers = get_numbers_tickets(1, 999, 7)
if lottery_numbers:
    print("Ваші лотерейні числа:", lottery_numbers)
