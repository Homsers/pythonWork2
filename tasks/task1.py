import random

numbers = 0
number0 = 0

random_number = random.randint(1, 9999)
print(random_number)

while random_number != 0:
    numbers = random_number % 10
    number0 = numbers + number0
    random_number = random_number // 10
print(f"сумма цифр: {number0} ")
