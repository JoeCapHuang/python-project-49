import random


def get_task() -> str:
    return 'What is the result of the expression?'


def get_random(unit: str) -> int:
    if unit == 'num':
        return random.randint(1, 50)

    elif unit == 'operator':
        return random.choice(["+", "-", "*"])


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
