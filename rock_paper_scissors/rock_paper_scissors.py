import random
import math

print("\nROCK_PAPER_SCISSORS\n")


def ini_parameter_func() -> tuple[list[str], int, str]:
    all_options = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf",
                   "sponge", "paper", "air", "water", "dragon", "devil", "lightning",
                   "gun"]
    opt = ["rock", "scissors", "paper"]
    sc = 0

    us_n = input("Enter your name: > ")
    print(f"Hello, {us_n}.")
    current_options = input("Please input game options in the format "
                            "\"symbol1,symbol2,symbol3,...\".\n> ").lower().split(",")
    current_options = list(set(current_options))

    if len(current_options) <= 2:
        print("Your input was too short!\nOptions will be: \"rock\", \"scissors\", \"paper\".")
    elif not any([current_options[i] in all_options for i in range(len(current_options))]):
        elements = str([current_options[i] in all_options for i in range(len(current_options))])
        print(f"Wrong some element ({elements})!\nOptions will be: \"rock\", \"scissors\", \"paper\".")
    else:
        opt_temp = []
        for j in range(len(all_options)):
            for i in range(len(current_options)):
                if all_options[j] == current_options[i]:
                    opt_temp.append(all_options[j])
        opt = opt_temp

    print("Okay, let's start!")

    return opt, sc, us_n


def program_answer_func(us_ch: str, sc: int) -> int:

    prog_ch = str(random.choice(options))

    win_ind = range((options.index(prog_ch) - math.floor(len(options) / 2)), (options.index(prog_ch)))
    win_options = [options[i] for i in win_ind]

    if prog_ch != us_ch and us_ch in win_options:
        print(f"Well done. The computer chose {prog_ch} and failed ")
        sc += 100

    elif prog_ch != us_ch and us_ch not in win_options:
        print(f"Sorry, but the computer chose {prog_ch}")

    else:
        print(f"There is a draw ({prog_ch})")
        sc += 50

    return sc


def rating_func(sc: int, us_n: str) -> int:

    all_players_res_list = []
    try:
        open('rating.txt')
    except FileNotFoundError as e:
        print(f"File {e} was not found. ")
    else:
        with open('rating.txt', 'r+t', encoding='utf-8') as my_file:
            all_players_res_list = my_file.readlines()

    sc_file = 0
    for s in all_players_res_list:
        if us_n in s:
            try:
                sc_file = int(s.split(" ")[-1])
            except TypeError:
                print("Score in your file rating.txt should be a number!")

    if sc <= sc_file:
        sc_res = sc_file

    else:
        sc_res = sc

    print(f"Your rating: {sc_res}")

    return sc_res


if __name__ == '__main__':

    options, score, user_name = ini_parameter_func()

    while True:
        user_choice = input("> ")

        if user_choice in options:
            score = program_answer_func(user_choice, score)

        elif user_choice == "!rating":
            score = rating_func(score, user_name)

        elif user_choice == "!exit":
            print("Bye!")
            exit()

        else:
            print("Invalid input. Please re-enter.")
