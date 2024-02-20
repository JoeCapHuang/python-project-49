from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def get_exercise_and_answer():
    first_number, second_number = nums = randint(1, 100), randint(1, 100)

    exercise = ' '.join(map(str, nums))
    answer = gcd(first_number, second_number)

    return exercise, answer
