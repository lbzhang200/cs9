from Beverage import Beverage 

class Coffee(Beverage):
    def __init__(self, ounces, price, style):
        super().__init__(self, ounces, price)
        self.style = style 

    def getInfo(self):
        return "{}, {}".format(self.style, super().getInfo())