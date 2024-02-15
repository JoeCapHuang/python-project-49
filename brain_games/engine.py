import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


GAME_ROUNDS = 3


def start_game(game):
    name = welcome_user()
    print(game.TASK)

    for _ in range(GAME_ROUNDS):
        exercise, correct_answer = game.get_exercise_and_answer()
        print(f'Question: {exercise}')
        answer = prompt.string('Your answer: ')

        if str(correct_answer) == answer:
            print('Correct!')

        else:
            print(f"{answer} is wrong answer ;(. Correct answer was "
                  f"{correct_answer}. Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
