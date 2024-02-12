from random import randint


def get_task() -> str:
    return 'Find the greatest common divisor of given numbers.'


def get_exercise():
    return randint(1, 100), randint(1, 100)


def get_correct_answer(exercise: tuple) -> int:
    first_number, second_number = exercise
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number

    return first_number + second_number
