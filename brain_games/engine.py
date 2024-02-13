import sys
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have you name? ')
    print(f'Hello, {name}!')
    return name


def make_string(exercise):
    if type(exercise) is not int:
        return ' '.join(map(str, exercise))
    else:
        return str(exercise)


def start_game(game):
    name = welcome_user()

    print(game.get_task())

    for i in range(3):
        exercise, correct_answer = game.get_exercise_and_answer()
        print(f'Question: {make_string(exercise)}')
        answer = prompt.string('Your answer: ')

        if str(correct_answer) == answer:
            print('Correct!')

        else:
            print(f"{answer} is wrong answer ;(. Correct answer was "
                  f"{correct_answer}. Let's try again, {name}!")
            sys.exit()

    print(f'Congratulations, {name}!')
