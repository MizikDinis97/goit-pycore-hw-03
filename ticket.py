import random

def get_numbers_tickets(min, max, quantity):
    return random.sample(range(min, max + 1), quantity)

lottery_numbers = get_numbers_tickets(1, 999, 7)
print("Ваші лотерейні числа:", lottery_numbers)
    