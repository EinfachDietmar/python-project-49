#!/usr/bin/env python3
from brain_games import cli # type: ignore
from .brain_games import main as greeting
import random


def main():
    greeting()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        random_num = random.randint(1, 9)
        random_first_num = random.randint(1, 10)
        random_second_num = random.randint(1, 7)
        first_num = random_num * random_first_num
        second_num = random_num * random_second_num
        div_list = []
        print(f'Question: {first_num} {second_num}')

        for n in range(1, max(first_num, second_num) + 1):
            if first_num % n == 0 and second_num % n == 0:
                div_list.append(n)
                continue
            else:
                continue

        player_input = int(input('Your answer: '))

        if player_input == max(div_list):
            i+= 1
            print('Correct!')
        else:
            return print(f"""'{player_input}' is wrong answer ;(. Correct answer was '{max(div_list)}'.
Let's try again, {cli.name}!""")
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
