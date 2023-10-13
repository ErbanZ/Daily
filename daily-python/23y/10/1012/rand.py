'''
Description: Generate a random number between the given start and end values.
Date: 2023-10-12 18:55:55
'''

import random

def generate_random_number(start: int, end: int)  -> int:
    return random.randint(start, end) % 10

random_number = generate_random_number(1, 100)
print(random_number * 10)
