import string
import random

valid_symbols = string.digits + string.ascii_letters


def create_random_key(n):
    key = ''
    for i in range(n):
        key += random.choice(valid_symbols)

    return key