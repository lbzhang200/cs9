class Item: 
    def __init__(self, upc = None, category = None, name = None, price = None):
        self.setUpc(upc)
        self.setCategory(category)

    def setUpc(self, upc):
        self.upc = upc 
    def setCategory(self, category):
        self.category = category if category is not None else None 
    def setName(self, name):
        self.name = name.upper() if name is not None else None 
    def setPrice(self, price):
        self.price = price 

    def toString():
        pricesstr = "{:.2f}".format(self.price) if self.price is not None else "None"
        return "UPC: {} Category: {} Name: {} Price: {}".format(self.upc, self.category, self.name, pricesstr)

    
