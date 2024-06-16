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
        x = ''
        if answer is True:
            x = 'yes'
        elif answer is False:
            x = 'no'

        inp = str(input('Your answer: ')).lower()

        if answer is True and inp == 'yes':
            i += 1
            print('Correct!')
        elif answer is False and inp == 'no':
            i += 1
            print('Correct!')
        else:
            return print(
                f"""'{inp}' is wrong answer ;(. Correct answer was '{x}'.
Let's try again, {cli.name}!""")
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
