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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    value = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return value


def print_report():
    print("Water:", resources.get("water"))
    print("Milk:", resources.get("milk"))
    print("Coffee:", resources.get("coffee"))
    print("Money:", resources.get("money"))


def check_resources(product):
    if resources.get("water") < product["ingredients"].get("water"):
        print("Sorry there is not enough water.")
        return False

    if resources.get("milk") < product["ingredients"].get("milk", 0):
        print("Sorry there is not enough milk.")
        return False

    if resources.get("coffee") < product["ingredients"].get("coffee"):
        print("Sorry there is not enough coffee.")
        return False

    return True


def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        product = MENU.get("espresso")

        if choice == "report":
            print_report()
            continue
        elif choice == "espresso":
            product = MENU.get("espresso")
        elif choice == "latte":
            product = MENU.get("latte")
        elif choice == "cappuccino":
            product = MENU.get("cappuccino")
        elif choice == "off":
            return
        else:
            print("Choice not valid expected: report/espresso/latte/cappuccino")
            continue

        if check_resources(product) is False:
            continue

        moneyInserted = insert_coins()

        change = round(moneyInserted - product.get("cost"), 2)
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
            continue

        print(f"Here is ${change} in change.")

        resources["money"] += product.get("cost")
        resources["water"] -= product["ingredients"].get("water")
        resources["coffee"] -= product["ingredients"].get("coffee")
        resources["milk"] -= product["ingredients"].get("milk", 0)

        print("Here is your espresso ☕️. Enjoy!")

    return

if __name__ == "__main__":
    main()
