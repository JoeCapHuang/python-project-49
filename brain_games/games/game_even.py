from random import randint


def get_task() -> str:
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_exercise() -> int:
    return randint(1, 100)


def get_correct_answer(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
