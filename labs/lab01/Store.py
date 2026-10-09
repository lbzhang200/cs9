from Item import Item 

class Store: 
    def __init__(self):
        self.items = {}

    def addItem(self, item):
        if item.category not in self.items:
            self.items[item.category] = [] 
        self.items[item.category].append(item)

    def removeItem(self, item):
        for category in self.items: #
            itemList = self.items[category]
            for i in range(len(itemList)):
                if itemList[i].upc == item.upc: 
                    itemList.pop(i)
                    return 

    def removeCategory(self, category):
        if category is not None:
            category = category.upper() #converting all to upper case to make sure its valid 
        if category in self.items:
            del self.items[category]

    def getItems(self, category):
        if category is not None:
            category = category.upper()
        if category not in self.items:
            return ""
        return "\n".join(item.toString() for item in self.items[category]) #new line inserted per each item 
            
    def doesItemExist(self, item): 
        for category in self.items:
            for existing in self.items[category]:
                if existing.upc == item.upc:
                    return True 
        return False 

    def countDollarItems(self):
        count = 0
        for category in self.items:
            for item in self.items[category]:
                if item.price is not None and item.price <= 1: 
                    count += 1 

        return count 


