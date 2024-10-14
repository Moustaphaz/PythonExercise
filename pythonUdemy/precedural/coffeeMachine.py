
logo ="""☕"""

MENU ={
    'espresso':{
        'ingredients':{
            'water':50,
            'coffee':18,
        },
        'cost':1.5,
    },
    'latte':{
        'ingredients':{
            'water':250,
            'milk':150,
            'coffee':24,
        },
        'cost':2.5
    },
    'cappuccino':{
        'ingredients':{
            'water':250,
            'milk':100,
            'coffee':24,
        },
        'cost':3,
    }
}

resources ={
    'water':500,
    'milk':200,
    'coffee':100,
    'money':0
}

profit =0

# TODO : 2.check if the resources is sufficient the make a drink
def check_resources(drink_name):
    """check if there is enough ingredients to make a drink...."""
    
    ingredients_and_cost =MENU[drink_name]['ingredients']
    for item in ingredients_and_cost:
        if ingredients_and_cost[item] >resources.get(item,0):
            print(f"not enough water in the coffee machine to make you {item}")
            return False
    return True
# TODO :3. Calculate the total amount of coins inserted
def process_coins():
    """Calculates the total amount of coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

#TODO: 4.make the drink if there enough ingredients in the coffee machine

def make_drink(drink_name):
    ingredients_need=MENU[drink_name]['ingredients']
    for item in ingredients_need:
        resources[item] -=ingredients_need[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

# Main Program

# TODO: 1.print a report of all the coffee machine resources

report =input("do you want to order a drink 'yes' or 'no' :\n").lower()
def print_report():
    if report =='yes':
        print("voici les ressource disponblie sur la machine a cafe:")
        for key,value in resources.items():
            if key =='coffee':
                print(f"{key}:{value}"+"g")
            elif key =='money':
                print(f"{key}:{value}"+"$")
            else:
                print(f"{key}:{value}"+"ml")
    else:
        print("vous aver choisi de ne pas commender")
        exit()
        
print_report()

is_on = True

while is_on:
    drink = input('What would you like? (espresso/latte/cappuccino): ').lower()
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
                    profit +=drink_cost
                
            else:
                print(f"Sorry, that's not enough money. Money refunded. ${payment}")
                print(f"your need ${drink_cost} to make a {drink} and you provide only{payment}")

        else:
            print("Cannot make the drink due to insufficient resources.")
            
    elif drink == 'report':
        print("Current resources:")
        for key, value in resources.items():
            if key =='coffee':
                print(f"{key.capitalize()}: {value}"+"g")
            elif key =='money':
                print(f"{key.capitalize()}: {profit}"+"$")
            else:
                print(f"{key.capitalize()}:{value}"+"ml")

    else:
        print("Invalid selection.")