class CoffeeMaker:
    """types of coffee that the machine makes"""
    
    def __init__(self):
        self.resources={
            'water':400,
            'milk':200,
            'coffee':100
        }
        
    def report(self):
        """print a report of all the resources available"""
        print(f"Water :{self.resources['water']}ml")
        print(f"Milk  :{self.resources['milk']}ml")
        print(f"Coffee :{self.resources['coffee']}g")
        
    def is_resources_sufficient(self, drink):
        """return true if there's enough ingredients to make the drink or false otherwise"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item]>self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    
    def make_coffee(self, order):
        """deducts the required ingredients from the resources of the coffee machine"""
        for item in order.ingredients:
            self.resources[item] -=order.ingredients[item]
        print(f"here is your {order.name} ☕. Enjoy!")