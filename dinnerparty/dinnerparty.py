import random

friends_count = 0
friends_list = {}
total = 0


def lucky_one_check():
    global friends_count
    choice = ""

    while choice.lower() != "yes" and choice.lower() != "no":
        choice = input("Who is lucky? feature? Write Yes/No:")

        if choice.lower() == "yes":
            lucky_one = random.randint(0, int(friends_count - 1))
            k = 0
            for i in friends_list:
                if friends_count > 1:
                    friends_list[i] = total / (friends_count - 1)
                    ...
                if k == lucky_one:
                    friends_list[i] = 0
                    print(i + " is lucky one! :) ")
                k += 1
                ...
            ...
        output_list()
        ...
    ...


def friend_input():
    global friends_count
    friends_count = int(input("Enter the number of friends joining (including you): "))

    if friends_count <= 0:
        print("No one is joined for the party!")
        return

    for i in range(friends_count):
        name = input("Enter the name of a person: ")
        friends_list[name] = 0
        ...
    total_amount_request()


def total_amount_request():
    global total
    total = int(input("Enter the total amount: "))
    divide()


def divide():
    global total
    global friends_count
    divided = total / friends_count
    for i in friends_list:
        friends_list[i] = divided
        ...
    lucky_one_check()


def output_list():
    global friends_list
    for z in friends_list:
        friends_list[z] = round(friends_list.get(z), 2)
        ...
    print(friends_list)


friend_input()
