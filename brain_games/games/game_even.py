from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_exercise_and_answer():
    exercise = randint(1, 100)

    answer = 'yes' if is_even(exercise) else 'no'

    return exercise, answer
