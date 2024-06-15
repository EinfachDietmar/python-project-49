#!/usr/bin/env python3
from brain_games import cli  # type: ignore
from .brain_games import main as greeting
import random


def is_prime(num):
    for ind in range(2, (num // 2) + 1):
        if num % ind == 0:
            return False
    return True


def main():
    greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        num = random.randint(0, 1000)
        print(f'Question: {num}')
        answer = is_prime(num)
        correct_answer = ''
        if answer is True:
            correct_answer = 'yes'
        elif answer is False:
            correct_answer = 'no'

        player_input = str(input('Your answer: ')).lower()

        if answer is True and player_input == 'yes':
            i += 1
            print('Correct!')
        elif answer is False and player_input == 'no':
            i += 1
            print('Correct!')
        else:
            return print(f"""'{player_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {cli.name}!""")
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
