import random


TASK = 'What is the result of the expression?'


def get_exercise_and_answer():
    exercise = (random.randint(1, 50), random.choice(["+", "-", "*"]),
                random.randint(1, 50))
    answer = None

    if exercise[1] == '+':
        answer = exercise[0] + exercise[2]

    elif exercise[1] == '-':
        answer = exercise[0] - exercise[2]

    elif exercise[1] == '*':
        answer = exercise[0] * exercise[2]

    return ' '.join(map(str, exercise)), answer
