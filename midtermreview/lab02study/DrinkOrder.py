class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        result = "Order Items: \n"
        count = 0 
        for drink in self.drinks:
            result += "* " + drink.getInfo() + "\n"
            count += drink.getPrice()

        result += "Total Price: ${:.2f}".format(count)
        return result 
