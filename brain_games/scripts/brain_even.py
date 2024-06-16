#!/usr/bin/env python3
from brain_games import cli  # type: ignore
from .brain_games import main as greeting
import random


def main():
    greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = random.randint(1, 101)
        print(f'Question: {random_number}')
        inp = str(input('Your answer: ')).lower()
        if random_number % 2 == 0 and inp == 'yes':
            i += 1
            print('Correct!')
        elif random_number % 2 != 0 and inp == 'no':
            i += 1
            print('Correct!')
        elif random_number % 2 == 1 and inp == 'yes':
            answer = 'no'
            return print(
                f"""'{inp}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {cli.name}!""")
        elif random_number % 2 == 0 and inp == 'no':
            answer = 'yes'
            return print(
                f"""'{inp}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {cli.name}!""")
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
