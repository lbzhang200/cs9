class DrinkOrder: 

    def __init__(self):
        self.drinks = [] 

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        result = "Order Items:\n"
        total = 0 
        for drink in self.drinks:
            result += "* " + drink.getInfo() + "\n"
            total += drink.getPrice()
        result += "Total Price: ${:.2f}".format(total)
        return result 