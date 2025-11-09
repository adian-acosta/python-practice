from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

running = True

while running:
    order = input(f"What would you like? ({menu.get_items()}): ").lower().strip()

    if order == 'report':
        coffee_maker.report()
        money_machine.report()
        print()
        continue
    elif order == "off":
        print('Turning off Q_Q...')
        running = False
        continue

    order = menu.find_drink(order)
    if order is not None:
        if not coffee_maker.is_resource_sufficient(order):
            continue
        if not money_machine.make_payment(order.cost):
            continue

        coffee_maker.make_coffee(order)

    print()