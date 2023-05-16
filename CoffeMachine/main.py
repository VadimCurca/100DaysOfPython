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


def check_resources(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice == "report":
            print_report()
            continue
        if choice == "off":
            return

        product = MENU.get(choice)

        if product is None:
            print("Choice not valid, expected: espresso/latte/cappuccino/report/off")
            continue
        if check_resources(product.get("ingredients")) is False:
            continue

        money_inserted = insert_coins()
        change = round(money_inserted - product.get("cost"), 2)
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
            continue

        for item in product["ingredients"]:
            resources[item] -= product.get("ingredients").get(item)
        resources["money"] += product.get("cost")

        print(f"Here is ${change} in change.")
        print("Here is your espresso ☕️. Enjoy!")

    return


if __name__ == "__main__":
    main()
