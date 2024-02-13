from random import randint


def get_task() -> str:
    return 'Find the greatest common divisor of given numbers.'


def get_exercise_and_answer():
    exercise = randint(1, 100), randint(1, 100)
    first_number, second_number = exercise

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    answer = first_number + second_number
    return exercise, answer
