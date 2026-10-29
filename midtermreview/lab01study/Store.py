from midtermreview.lab01study.Item import Item 

class Store(Item): 
    def __init__(self):
        self.items = {}

    def addItem(self, item):
        if item.category not in self.items:
            self.items[item.category] = [] 
        self.items[item.category].append(item)

    def removeItem(self, item):
        for category in self.items: #finding the category 
            itemList = self.items[category] #locating the itemlist based on each category 
            for i in range(len(itemList)): #looping through the individual itemlist 
                if itemList[i].upc == item.upc: #finding the upc location vs item.upc 
                    itemList.pop(i) #popping if they are the same 
                    return 

    def removeCategory(self, category):
        if category is not None:
            category = category.upper() 
        if category in self.items:
            del self.item[category]

    def getItems(self, category):
        if category is not None:
            category = category.upper()
        if category not in self.items:
            return ""
        return "\n".join(item.toString() for item in self.items[category])


    def doesItemExist(self, item):
        count = 0 
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