from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NOT_PRIME = 0
FIRST_PRIME_NUMBER = 2


def is_prime(num: int) -> bool:
    numbers = [i for i in range(num + 1)]
    numbers[1] = NOT_PRIME
    prime_nums = []

    i = FIRST_PRIME_NUMBER
    while i <= num:
        if numbers[i] != NOT_PRIME:
            prime_nums.append(numbers[i])
            for j in range(i, num + 1, i):
                numbers[j] = NOT_PRIME
        i += 1
    return num in prime_nums


def get_exercise_and_answer():
    exercise = randint(1, 50)

    if is_prime(exercise):
        answer = 'yes'

    else:
        answer = 'no'

    return exercise, answer
