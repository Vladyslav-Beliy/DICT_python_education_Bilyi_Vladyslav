import random
import operator
from datetime import datetime


class RandomTest:
    @staticmethod
    def second_stage():
        marks = 0
        tests = 0
        number_of_tests = 5
        value_error = 0
        while tests < number_of_tests:
            tests = tests + 1
            x = random.randint(2, 10)
            y = random.randint(2, 10)
            sign_list = {'+': operator.add,
                         '-': operator.sub,
                         '*': operator.mul}
            sign = random.choice(list(sign_list.keys()))
            res = (x, sign, y)
            answer = (sign_list.get(sign)(x, y))
            print(*res)

            client_input = input('>')
            try:
                if int(client_input) == answer:
                    print('Right!')
                    marks = marks + 1
                elif int(client_input) != answer:
                    print('Wrong!')
            except ValueError:
                print('Incorrect format\nTry numbers')
                value_error += 1
                number_of_tests += 1

            if tests == number_of_tests:
                corrected_amount_of_test = number_of_tests - value_error
                final = (f'Your mark is {marks}/{corrected_amount_of_test}\n'
                         f'ValueErrors - ({value_error})')
                print(final)
                print("Would you like to save your result to file\nEnter\nyes or no")
                results_file_input = input('>')
                if results_file_input.lower().strip() == 'yes':
                    with open("Results File.txt", "a") as text_write:
                        now = datetime.now()
                        dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
                        text_input = input("Enter your name: >")
                        text_input_group = input("Enter your group: >" )
                        text_write.write(f"\n\n{text_input} {text_input_group}"
                                         f" Simple arithmetic operations with"
                                         f" numbers from 2 to 9-{final} "
                                         f"\nDate and time of test {dt_string}")

    @staticmethod
    def third_stage():
        marks = 0
        tests = 0
        number_of_tests = 5
        value_error = 0
        while tests < number_of_tests:
            tests = tests + 1
            x = random.randint(11, 29)
            res = (f'{x}^2')
            answer = (x**2)
            print(res)
            client_input = input('>')
            try:
                if int(client_input) == answer:
                    print('Right!')
                    marks = marks + 1
                elif int(client_input) != answer:
                    print('Wrong!')
            except ValueError:
                print('Incorrect format\nTry numbers')
                value_error += 1
                number_of_tests += 1
            try:
                if tests == number_of_tests:
                    corrected_amount_of_test = number_of_tests - value_error
                    final = (f'Your mark is {marks}/{corrected_amount_of_test}\n'
                             f'ValueErrors - ({value_error})')
                    print(final)
                    print("Would you like to save your result to file\nEnter\nyes or no")
                    results_file_input = input('>')
                    if results_file_input.lower().strip() == 'yes':
                        with open("Results File.txt", "a") as text_write:
                            now = datetime.now()
                            dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
                            text_input = input("Enter your name: >")
                            text_input_group = input("Enter your group")
                            text_write.write(f"\n\n{text_input} {text_input_group}"
                                            f" Squaring numbers from 11 to 29-{final}"
                                            f"\nDate and time of test {dt_string}")
            except ValueError:
                print('Please use number')


class Menu:

    @staticmethod
    def welcome():
        print('Виберіть рівень складності\n'
              '1. Прості арифметичні операції з числами від 2 до 9\n'
              '2. Зведення у квадрат чисел від 11 до 29' )
        menu_input = input('>')
        if menu_input == '1':
            RandomTest.second_stage()
        elif menu_input == '2':
            RandomTest.third_stage()
        else:
            print('Enter only numbers from Menu')


while True:
    Menu.welcome()
