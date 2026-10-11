from Item import Item

class Store:
    def __init__(self):
        self.items = {}
    
    def addItem(self, item):
        if item.category not in self.items:
            self.items[item.category] = [] 
        self.items[item.category].append(item) #else just append the item 

    def removeItem(self, item):
        for category in self.items: #loop trhoguh the categories in self.items 
            itemList = self.items[category] #loops through each category 
            for i in range (len(itemList)):
                if itemList[i].upc == item.upc: 
                    itemList.pop(i)
                    return 

    def removeCategory(self, category): 
        if category is not None:
            category = category.upper()
        if category in self.items:
            del self.items[category]


    def getItems(self, category):
        if category is not None:
            category = category.upper()
        if category in self.items:
            return "\n".join(Item.toString() for item in self.items[category]) # loops through category and returns item to string method 
        else:
            return ""
        
    def doesItemExist(self, item):
        for category in self.items:
            itemList = self.items[category]
            for i in range(len(itemList)):
                if itemList[i].upc == item.upc:
                    return True 
        return False 


    def countDollarItems(self):
        for category in self.items:
            for items in self.items[category]:
                if items.price is not None and items.price <= 1:
                    count += 1 
        return count 
                
