import sys
import prompt
import importlib


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have you name? ')
    print(f'Hello, {name}!')
    return name


def lose_game(name, answer, correct_answer):
    print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}. Let's try again, {name}!")
    sys.exit()


def game_cycle(game):
    name = welcome_user()
    game_module = importlib.import_module("brain_games.games.%s" % game)

    print(game_module.get_task())

    for i in range(3):
        exercise = game_module.get_exercise()
        print(f'Question: {exercise}')
        answer = prompt.string('Your answer: ')
        correct_answer = str(game_module.get_correct_answer(exercise))

        if correct_answer == answer:
            print('Correct!')

        else:
            lose_game(name, answer, correct_answer)

    print(f'Congratulations, {name}!')
