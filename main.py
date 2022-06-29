# Imports
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Functions
def get_order():
    """
    Prompts user for an order or key command.
    Checks command is valid or input inside menu.
    Returns validated item.
    """
    valid_input = False
    while not valid_input:
        order = input("Enter your choice? ").lower()
        if order != 'off' and order != 'report' and order not in my_menu.get_items():
            print("You did not enter an item from the menu.")
            continue
        return order


my_coffee_machine = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

vending = True
while vending:
    options = my_menu.get_items().title()
    options_list = options.split("/")
    print(f"What would you like: {' '.join(options_list)}")
    order_name = get_order()
    if order_name == 'off':
        vending = False
    elif order_name == 'report':
        my_coffee_machine.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(order_name)
        if my_coffee_machine.is_resource_sufficient(drink):
            my_money_machine.make_payment(drink.cost)
            my_coffee_machine.make_coffee(drink)
