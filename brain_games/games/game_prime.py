from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_PRIME_NUMBER = 2
NOT_PRIME = 1


def is_prime(num: int) -> bool:
    if num <= NOT_PRIME:
        return False
    for i in range(FIRST_PRIME_NUMBER, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_exercise_and_answer():
    exercise = randint(1, 50)

    answer = 'yes' if is_prime(exercise) else 'no'

    return exercise, answer
