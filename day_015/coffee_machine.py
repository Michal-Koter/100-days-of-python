MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
    "pennies": 0.01
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_report():
    """Print a report of resources and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def make_coffee(drink_name):
    """Make a coffee, if it isn't possible return None"""
    current_drink = MENU[drink_name]

    if not is_resource_sufficient(current_drink["ingredients"]):
        return None

    payment = process_coin()
    if not is_transaction_successful(payment, current_drink["cost"]):
        return None

    reduce_resource(current_drink["ingredients"])

    print(f"Here is your {drink_name} ☕. Enjoy!")


def is_resource_sufficient(order_ingredients: dict) -> bool:
    """Returns True when order can be made, False if ingredients are insufficient."""
    for key, value in order_ingredients.items():
        if resources[key] < value:
            print(f"Sorry there is not enough {key}.")
            return False

    return True


def process_coin() -> float:
    """Returns the total calculated from coins inserted."""
    total = 0

    for key, value in COINS.items():
        inserted = input(f"How much {key}?: ")
        inserted = int(inserted) if inserted.isdigit() else 0
        total += inserted * value

    return total


def is_transaction_successful(received: float, cost: float) -> bool:
    """Return True when the payment is accepted, or False if money is insufficient."""
    global profit

    if received < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = received - cost
    print("Here is ${:.2f} dollars in change.".format(change))

    profit += cost

    return True


def reduce_resource(ingredients: dict):
    """Deduct the required ingredients from the resources."""
    global resources

    for key, value in ingredients.items():
        resources[key] -= value


if __name__ == "__main__":
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in MENU:
            make_coffee(choice)
        elif choice == "report":
            show_report()
        elif choice == "off":
            break
        else:
            print("Wrong choice. Please try again.")