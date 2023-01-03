field = {}


def start():
    global field
    list_inp = list("_" * 9)
    field = get_d(list_inp)
    player = "X"

    print(get_field())
    while check_game() == 3:
        input_coordinates(player)
        player = change_player(player)
        ...
    print(get_result())
    ...


def check_game():
    game_list = list(field.values())

    ln = len(game_list)
    st = 3

    for i in range(0, ln, 3):
        if game_list[i] == game_list[i + 1] == game_list[i + 2]:
            if game_list[i] != "_":
                st = find_winner(st, game_list[i])
            ...
        ...
    for i in range(0, 3):
        if game_list[i] == game_list[i + 3] == game_list[i + 6]:
            if game_list[i] != "_":
                st = find_winner(st, game_list[i])
            ...
        ...
    if game_list[0] == game_list[4] == game_list[8]:
        if game_list[0] != "_":
            st = find_winner(st, game_list[0])
        ...
    if game_list[2] == game_list[4] == game_list[6]:
        if game_list[2] != "_":
            st = find_winner(st, game_list[2])
        ...
    if "_" not in game_list and st == 3:
        st = 0
        ...

    return st


def get_d(inp_list: list):
    column = 1
    roll = 1

    for i in range(len(inp_list)):
        if roll > 3:
            column += 1
            roll = 1
            ...
        key = "{0}{1}".format(column, roll)
        field[key] = inp_list[i]
        roll += 1
        ...
    return field


def find_winner(st: int, symbol: str):
    if st == 3:
        st = 1 if symbol == "X" else 2
        ...
    else:
        st = -1
        ...
    return st


def get_field():
    list_inp = list(field.values())
    f_inp = ""

    for i in range(0, len(list_inp), 3):
        game_str = "| {0} {1} {2} |\n".format(list_inp[i], list_inp[i + 1], list_inp[i + 2])
        f_inp += game_str
        ...
    f_inp = f_inp.replace("_", " ")
    game_field = f"---------\n{f_inp}---------"
    return game_field


def get_result():
    msg_list = ["Impossible", "No one Win", "X wins", "O wins"]
    result = check_game()
    return msg_list[result + 1]


def input_coordinates(plr: str):
    enter = False

    while not enter:
        inp = input(f"Enter the coordinates {plr}: ").strip()
        val = field.get(inp)
        if val == "X" or val == "O":
            print("This cell is occupied! Choose another one!")
        elif not inp.replace(" ", "").isnumeric():
            print("You should enter numbers!")
        elif val is None:
            print("Coordinates should be from 1 to 3!")
        else:
            field.update({inp: plr})
            enter = True
            print(get_field())


def change_player(plr: str):
    if plr == "X":
        return "O"
    else:
        return "X"


start()
