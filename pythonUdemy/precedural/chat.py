logo = """☕"""

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 250,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3,
    }
}

resources = {
    'water': 500,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

profit = 0

# TODO : 2.check if the resources is sufficient the make a drink
def check_resources(drink_name):
    """check if there is enough ingredients to make a drink...."""

    ingredients_and_cost = MENU[drink_name]['ingredients']
    for item in ingredients_and_cost:
        if ingredients_and_cost[item] > resources.get(item, 0):
            print(f"Not enough {item} in the coffee machine to make {drink_name}")
            return False
    return True

# TODO :3. Calculate the total amount of coins inserted
def process_coins():
    """Calculates the total amount of coins inserted."""
    print("Please insert coins:")
    total = 0
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            total += quarters * 0.25
            dimes = int(input("How many dimes?: "))
            total += dimes * 0.10
            nickels = int(input("How many nickels?: "))
            total += nickels * 0.05
            pennies = int(input("How many pennies?: "))
            total += pennies * 0.01
            break
        except ValueError:
            print("Invalid input. Please enter a valid number of coins.")
    return total

# TODO: 4.make the drink if there enough ingredients in the coffee machine
def make_drink(drink_name):
    ingredients_need = MENU[drink_name]['ingredients']
    for item in ingredients_need:
        resources[item] -= ingredients_need[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

# Main Program

# TODO: 1.print a report of all the coffee machine resources
def print_report():
    print("Current resources:")
    for key, value in resources.items():
        if key == 'coffee':
            print(f"{key.capitalize()}: {value}"+"g")
        elif key == 'money':
            print(f"{key.capitalize()}: {profit}"+"$")
        else:
            print(f"{key.capitalize()}:{value}"+"ml")

# User Interface
def show_menu():
    print("Menu:")
    for drink in MENU:
        print(f"- {drink}: {MENU[drink]['cost']}{currency}")

# Inventory Management
def restock_inventory():
    for item in resources:
        if resources[item] < resources.get('restock_level', 100):
            print(f"Restocking {item}...")
            resources[item] = resources.get('restock_quantity', 500)

# Currency
currency = "USD"  # Adjust to your desired currency

is_on = True

while is_on:
    show_menu()
    drink = input('What would you like? (espresso/latte/cappuccino/off/report): ').lower()

    if drink == 'off':
        is_on = False
        print("Turning off the coffee machine. Goodbye!")

    elif drink in MENU:
        if check_resources(drink):
            payment = process_coins()
            drink_cost = MENU[drink]['cost']
            if payment >= drink_cost:
                change = round(payment - drink_cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                make_drink(drink)
                profit += drink_cost
            else:
                print(f"Sorry, that's not enough money. Money refunded. ${payment}")
        else:
            print("Cannot make the drink due to insufficient resources.")

    elif drink == 'report':
        print_report()
        restock_inventory()  # Check and restock inventory if needed

    else:
        print("Invalid selection.")