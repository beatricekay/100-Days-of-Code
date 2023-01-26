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
}

def check_resources(drink_choice):
    '''Checks if there are sufficient resources and deducts the resources accordingly.'''
    # Deduction of resources cannot occur here as the customer has to have enough money before the coffee can be prepared
    
    ingredients = MENU[drink_choice]['ingredients']

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True
        
profit = 0

def process_coins(drink_choice):
    '''Checks if the payment is enough.'''

    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies

    drink_cost = MENU[drink_choice]['cost']
    ingredients = MENU[drink_choice]['ingredients']

    # Accept payment and return change if applicable
    if total >= drink_cost:
        change = round(total - drink_cost,2)
        global profit
        profit += drink_cost

        # Serve coffee and deduct resources
        for item in ingredients:
            resources[item] -= ingredients[item]

        print(f"Here is ${change} in change.")
        print(f"Here is your {drink_choice}. Enjoy!")
    
    else:
        print("Sorry that's not enough money. Money refunded.")



is_on = True
while is_on:

    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if drink_choice == "off":
        is_on = False

    elif drink_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        # Resources enough, move on to payment stage
        if check_resources(drink_choice) == True:
            print("Please insert coins.")
            process_coins(drink_choice)

# To consider splitting coin processing and coffee preparation