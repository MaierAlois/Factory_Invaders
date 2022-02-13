from random import randint

def lerp(actual, alpha, target, yposition = 360):
    return [actual[0] + ((target[0] - actual[0]) * alpha), yposition]

def get_random_col():
    return randint(0, 3)