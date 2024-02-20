import random


TASK = 'What is the result of the expression?'


def get_exercise_and_answer():
    first_number = random.randint(1, 50)
    second_number = random.randint(1, 50)
    operator = random.choice(["+", "-", "*"])

    exercise = (first_number, operator, second_number)
    answer = None

    if operator == '+':
        answer = first_number + second_number

    elif operator == '-':
        answer = first_number - second_number

    elif operator == '*':
        answer = first_number * second_number

    return ' '.join(map(str, exercise)), answer
