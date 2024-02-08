from random import randint
import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have you name? ')
    print(f'Hello, {name}!')
    return name


def game_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = randint(1, 100)

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if correct_answer == answer.lower():
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}. Let's try again, Bill!")
            sys.exit()
    print(f'Congratulations, {name}!')
