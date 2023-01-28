from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


bea_coffee_maker = CoffeeMaker()
bea_money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    # 1. Take input from customer
    options = menu.get_items()
    drink_choice = input(f"What would you like? ({options}): ")

    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        bea_coffee_maker.report()
        bea_money_machine.report()
    else:
        drink = menu.find_drink(drink_choice)

        # Prompt user to select another item if not available on the menu
        if drink is None:
            print("Choose another item.")
        
        # 2. Check if resources are sufficient and # 3. Process coins and # 4. Check if transaction is successful
        elif bea_coffee_maker.is_resource_sufficient(drink) and bea_money_machine.make_payment(drink.cost):
            # 5. Make coffee
            bea_coffee_maker.make_coffee(drink)
        




