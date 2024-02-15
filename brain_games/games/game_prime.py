from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    prime_numbers = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                     43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    if num in prime_numbers:
        return True
    else:
        return False


def get_exercise_and_answer():
    exercise = randint(1, 100)

    if is_prime(exercise):
        answer = 'yes'

    else:
        answer = 'no'

    return exercise, answer
