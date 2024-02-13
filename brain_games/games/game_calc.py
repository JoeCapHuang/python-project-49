import random


def get_task() -> str:
    return 'What is the result of the expression?'


def get_random(unit: str) -> int:
    if unit == 'num':
        return random.randint(1, 50)

    elif unit == 'operator':
        return random.choice(["+", "-", "*"])


def get_exercise_and_answer():
    exercise = get_random('num'), get_random('operator'), get_random('num')
    answer = None

    if exercise[1] == '+':
        answer = exercise[0] + exercise[2]

    elif exercise[1] == '-':
        answer = exercise[0] - exercise[2]

    elif exercise[1] == '*':
        answer = exercise[0] * exercise[2]

    return exercise, answer


# def get_correct_answer(exercise: tuple) -> int:
#     if exercise[1] == '+':
#         return exercise[0] + exercise[2]
#
#     elif exercise[1] == '-':
#         return exercise[0] - exercise[2]
#
#     elif exercise[1] == '*':
#         return exercise[0] * exercise[2]
