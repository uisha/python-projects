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
    "money" : 0,
}


def report():
    print(f"\n    Water: {resources['water']}ml")
    print(f"    Milk: {resources['milk']}ml")
    print(f"    Coffee: {resources['coffee']}ml")
    print(f"    Money: ${resources['money']}\n")


def check_resources(drink):
    """returns True if there are enough resources... pag kulang, return False"""
    if 'milk' in MENU[drink]['ingredients']:
        drink_water = MENU[drink]['ingredients']['water']
        drink_milk = MENU[drink]['ingredients']['milk']
        drink_coffee = MENU[drink]['ingredients']['coffee']

        if resources['water'] < drink_water:
            print("   Sorry, there is not enough water.")
            condition = False
        elif resources['milk'] < drink_milk:
            print("   Sorry, there is not enough milk.")
            condition = False
        elif resources['coffee'] < drink_coffee:
            print("   Sorry, there is not enough coffee.")
            condition = False
        else:
            condition = True
    else:
        drink_water = MENU[drink]['ingredients']['water']
        drink_coffee = MENU[drink]['ingredients']['coffee']

        if resources['water'] < drink_water:
            print("   Sorry, there is not enough water.")
            condition = False
        elif resources['coffee'] < drink_coffee:
            print("   Sorry, there is not enough coffee.")
            condition = False
        else:
            condition = True

    return condition


def make_coffee(drink):
    if 'milk' in MENU[drink]['ingredients']:
        resources['milk'] -= MENU[drink]['ingredients']['milk']

    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    resources['water'] -= MENU[drink]['ingredients']['water']

    resources['money'] += MENU[drink]['cost']


print("""
MENU
Espresso: $1.5
Latte: $2.5
Cappuccino: $3.0
""")

machine_is_off = False


while machine_is_off == False:
    prompt = ''
    while prompt != 'espresso' and prompt != 'latte' and prompt != 'cappuccino' and prompt != 'report' and prompt != 'off':
        prompt = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
    if prompt == 'off':
        machine_is_off = True
    elif prompt == 'report':
        report()
    else:
        if check_resources(prompt) == True:
            quarter_payment = int(input("    How many quarters?: "))
            dime_payment = int(input("    How many dimes?: "))
            nickle_payment = int(input("    How many nickles?: "))
            penny_payment = int(input("    How many pennies?: "))

            total_payment = (quarter_payment * 0.25) + (dime_payment * 0.10) + (nickle_payment * 0.05) + (penny_payment * 0.01)

            if total_payment < MENU[prompt]['cost']:
                print("There is not enough money, money has been refunded.")
            elif total_payment == MENU[prompt]['cost']:
                print("Thank you for paying the exact amount!")
            else:
                change = total_payment - MENU[prompt]['cost']
                print(f"Here is ${round(change, 2)} in change.")

            print(f"\n    Here is your {prompt}!\n")
            make_coffee(prompt)


print("exit")