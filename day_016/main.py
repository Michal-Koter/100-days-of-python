from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



if __name__ == "__main__":
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True
    while is_on:
        option = input(f"What would you like? {menu.get_items()}:")
        if option == "off":
            is_on = False
        elif option == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(option)
            if drink is None:
                continue

            if not coffee_maker.is_resource_sufficient(drink):
                continue

            if not money_machine.make_payment(drink.cost):
                continue

            coffee_maker.make_coffee(drink)
