from random import randint


def get_task() -> str:
    return 'What number is missing in the progression?'


def get_exercise_and_answer():
    beginning, end, step = (randint(1, 15), randint(85, 100), randint(2, 8))

    raw_progression = list(range(beginning, end, step))

    if len(raw_progression) > 10:
        progression = raw_progression[:10]
        max_index = len(progression) - 1
    else:
        progression = raw_progression
        max_index = len(raw_progression) - 1

    random_index = randint(0, max_index)
    answer = progression[random_index]
    progression[random_index] = '..'
    exercise = progression
    return exercise, answer
