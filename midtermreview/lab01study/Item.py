class Item: 

    def __init__(self, upc=None, category=None, name=None, price=None):
        self.setUpc(upc)
        self.setCategory(category)
        self.setName(name)
        self.setPrice(price)

    def setUpc(self, upc ):
        self.upc = upc 

    def setCategory(self, category):
        self.category = category.upper()

    def setName(self, name):
        self.name = name.upper()

    def setPrice(self, price):
         self.price = price 

    def toString(self): 
        pricesstr = "{:.2f}".format(self.price) if self.price is not None else "None"
        return "UPC: {}, Category: {}, Name: {}, Price: ${}".format(self.upc, self.category, self.name, pricesstr)


     

