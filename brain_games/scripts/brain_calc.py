#!/usr/bin/env python3
from brain_games import cli  # type: ignore
from .brain_games import main as greeting
import random


def main():
    greeting()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        random_first_num = random.randint(0, 100)
        random_second_num = random.randint(0, 100)
        random_sign = random.choice(('-', '+', '*'))
        print(f'Question: {random_first_num} {random_sign} {random_second_num}')
        inp = int(input('Your answer: '))
        if random_sign == '-':
            answer = random_first_num - random_second_num
        elif random_sign == '+':
            answer = random_first_num + random_second_num
        elif random_sign == '*':
            answer = random_first_num * random_second_num
        if inp == answer:
            i += 1
            print('Correct!')
        else:
            return print(
                f"""'{inp}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {cli.name}!""")
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
