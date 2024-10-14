class MoneyMachine:
    
    CURRENCY ='$'
    
    COINS_VALUES={
        'quarters':0.25,
        'dimes':0.10,
        'nickles':0.05,
        'pennies':0.01
    }
    
    def __init__(self):
        self.profit =0
        self.money_received =0
    
    def report(self):
        """print the current profit"""
        print(f"Money :{self.CURRENCY}{self.profit}")
    
    def process_coins(self):
        """return tho total amount of insert coins"""
        print("please insert coins.")
        for coin in self.COINS_VALUES:
            self.money_received +=int(input(f"how many {coin}?:"))*self.COINS_VALUES[coin]
        return self.money_received
    
    def make_payment(self,cost):
        """return true if payment accept or false if not"""
        self.process_coins()
        if self.money_received >=cost:
            change =round(self.money_received-cost,2)
            print(f"here is the {self.CURRENCY}{change} in change.")
            self.profit+=cost
            self.money_received =0
            return True
        else:
            print(f"Sorry that's not enough money the cost is {cost} , Money refound.{self.money_received}")
            self.money_received =0
            return False
    
    pass

