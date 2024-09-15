
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
coffee_machine = True

while coffee_machine:
    option = menu.get_items()
    choice = input(f"Which coffee you want? ({option}): ")
    if choice == "off":
        print("Okay, have a great day ahead!")
        coffee_machine = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(drink.cost) :
            coffee_maker.make_coffee(drink)

