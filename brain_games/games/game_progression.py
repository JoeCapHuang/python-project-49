from random import randint


TASK = 'What number is missing in the progression?'
MIN_ELEMENTS = 5
MAX_ELEMENTS = 10


def get_exercise_and_answer():
    beginning, step = (randint(1, 15), randint(2, 8))

    progression = []

    for _ in range(randint(MIN_ELEMENTS, MAX_ELEMENTS)):
        progression.append(beginning)
        beginning += step

    max_index = len(progression) - 1

    random_index = randint(0, max_index)
    answer = progression[random_index]
    progression[random_index] = '..'
    exercise = ' '.join(map(str, progression))
    return exercise, answer
