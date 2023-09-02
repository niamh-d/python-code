from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

selection = menu.get_items()

machine_on = True

while machine_on:

    drink_selected = input(f"Choose a drink {selection}: ")

    if drink_selected == "off":
        machine_on = False
        print("Goodbye!")
    elif drink_selected == "report":
        print(CoffeeMaker().report())
    else:
        drink = menu.find_drink(drink_selected)
        print("The price is ${:0.2f}. Please insert coins.".format(drink.cost))

        if CoffeeMaker.is_resource_sufficient(drink_selected.ingredients):
            print("yes")