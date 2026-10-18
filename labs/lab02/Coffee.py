from Beverage import Beverage 
class Coffee(Beverage):

    def __init__(self, ounces, price, style):
        super().__init__(ounces, price)
        self.style = style 

    def getInfo(self):
        return "{} Coffee, {}".format(self.style, super().getInfo()) 