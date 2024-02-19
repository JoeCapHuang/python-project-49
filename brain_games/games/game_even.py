from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_exercise_and_answer():
    exercise = randint(1, 100)

    if is_even(exercise):
        answer = 'yes'

    else:
        answer = 'no'

    return exercise, answer
