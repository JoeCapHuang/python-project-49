from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_exercise_and_answer():
    exercise = randint(1, 100)

    if exercise % 2 == 0:
        answer = 'yes'

    else:
        answer = 'no'

    return exercise, answer
