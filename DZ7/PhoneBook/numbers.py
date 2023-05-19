import random


def create_number():
    number = '+7'
    for i in range(10):
        number += str(random.randint(0, 9))
    return number
