#!/usr/bin/env python3
from brain_games import cli  # type: ignore
from .brain_games import main as greeting
import random


def main():
    greeting()
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        num_one = random.randint(0, 100)
        step = random.randint(2, 7)
        length = random.randint(5, 11)
        num_two = num_one + (step * length)
        num_list = []
        for n in range(min(num_one, num_two), max(num_one, num_two), step):
            num_list.append(n)

        index = random.randint(0, len(num_list) - 1)
        num = num_list[index]
        hidden_num = num_list
        for ind, number in enumerate(num_list):
            if number == num:
                hidden_num[ind] = '..'

        print(f'Question: {" ".join(str(x) for x in hidden_num)}')
        inp = int(input('Your answer: '))
        if inp == num:
            i += 1
            num_list = []
            print('Correct!')
        else:
            return print(
                f"""'{inp}' is wrong answer ;(. Correct answer was '{num}'.
Let's try again, {cli.name}!""")
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
