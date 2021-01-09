from math import sqrt, floor


def nearest_square(num):
    return (floor(sqrt(num)) ** 2) if num > 0 else 0
