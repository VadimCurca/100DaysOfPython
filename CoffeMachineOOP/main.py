from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffe_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        choice = input(f"What would you like? ({menu.get_items()}):")

        if choice == "off":
            return
        if choice == "Report":
            coffe_maker.report()
            money_machine.report()
            continue

        drink = menu.find_drink(choice)

        if drink is None:
            continue
        if coffe_maker.is_resource_sufficient(drink) is False:
            continue
        if money_machine.make_payment(drink.cost) is False:
            continue

        coffe_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
