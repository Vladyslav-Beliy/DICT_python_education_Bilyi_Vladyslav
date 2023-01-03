
espresso = {"water": 250, "milk": 0, "beans": 16, "money": 4}
latte = {"water": 350, "milk": 75, "beans": 20, "money": 7}
capuccino = {"water": 200, "milk": 100, "beans": 12, "money": 6}


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def start_machine(self):
        menu = "Write action (buy, fill, take, remaining, exit): "
        action = input(menu).strip().lower()

        while action != "exit":
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take_money()
            elif action == "remaining":
                self.print_state()
            else:
                print("Incorrect selection")

            menu = "Write action (buy, fill, take, remaining, exit): "
            action = input(menu)

    def print_state(self):
        print("The coffee machine has: "
              "\n{0} of water \n{1} of milk \n{2} of coffee beans \n{3} of disposable cups \n{4} of money"
              .format(self.water, self.milk, self.beans, self.cups, self.money))

    def capacity(self, coffee):
        msg = True
        if self.cups < 1:
            print("Not enough cups")
            msg = False
        if self.water < coffee.get("water"):
            print("Not enough water")
            msg = False
        if self.milk < coffee.get("milk"):
            print("Not enough milk")
            msg = False
        if self.beans < coffee.get("beans"):
            print("Not enough beans")
            msg = False
        return msg

    def buy(self):
        menu = "What do you want to buy? \n1 - espresso \n2 - latte \n3 - capuccino \nback – to main menu:"

        selection = input(menu)

        if selection == "1":
            if self.capacity(espresso):
                self.get_drink(espresso)
        elif selection == "2":
            if self.capacity(latte):
                self.get_drink(latte)
        elif selection == "3":
            if self.capacity(capuccino):
                self.get_drink(capuccino)
        elif selection == "back":
            print("Going back to main menu")
        else:
            print("Wrong selection, try again")

    def get_drink(self, coffee):
        print("I have enough resources, making you a coffee!")

        self.money += coffee.get("money")
        self.water -= coffee.get("water")
        self.milk -= coffee.get("milk")
        self.beans -= coffee.get("beans")
        self.cups -= 1

    def fill(self):
        water = int(input("Write how many ml of water do you want to add:"))
        milk = int(input("Write how many ml of milk do you want to add: "))
        beans = int(input("Write how many grams of coffee beans do you want to add: "))
        cups = int(input("Write how many disposable cups of coffee do you want to add: "))

        self.cups = self.cups + cups
        self.water = self.water + water
        self.milk = self.milk + milk
        self.beans = self.beans + beans

    def take_money(self):
        print("I gave you {}".format(self.money))
        self.money = 0


coffee_machine = CoffeeMachine()
coffee_machine.start_machine()
