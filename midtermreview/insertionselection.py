#selection sort is finding the max and moving it to the right, then scanning and finding the next max 

def selectionSort(aList): 
    for fillslot in range(len(aList) -1, -1, -1): #looks at the last index (should be the largest) 
        posofMax = 0 
        for location in range(1, fillslot + 1):
            if aList[location] > aList[posofMax]: #looks for the largest
                posofMax = location #updates posmax to the largest 

        temp = aList[fillslot] #replaces fillsalot(last index) with the largest number 
        aList[fillslot] = aList[posofMax]
        aList[posofMax] = temp


#insertion sort is finding sorting the left so the leftside si always sorted, and then looking at the right for where to put it so really scans from left to right 

def insertionSort(aList):
    for index in range(1, len(aList)): #loops through the list 

        currentvalue = aList[index] #sets current value to one 
        position = index # current index 

        while position > 0 and aList[position - 1] > currentvalue: #checks if the left is greater than the right 
            aList[position]  = aList[position - 1] #if yes, switch 
            position = position - 1  #swtich position 

        aList[position] = currentvalue #updates alist with current vlaue so smaller is in the front and larger is in the back



#nodes and linked lists 

##class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None 

    def getData(self):
        return self.data #looking for data 

    def getNext(self):
        return self.next #looking for node 

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


#class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None 

    def addToFront(self, item):
        temp = Node(item) #take the temp node 
        temp.setNext(self.head) #set next node to the self.head 
        self.head = temp 

    def length(self):
        temp = self.head
        count = 0 
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count 


    def search(self, item):
        temp = self.head
        found = False 
        while temp != None and not found:
            if temp.getData() == item:
                found = True 
            else:
                temp = temp.getNext()
        return found 

    def remove(self, item):
        current = self.head

        if current == None:
            return 

        previous = None 
        found = False 

        while not found:
            if current == None:
                return 
            if current.getData() == item:
                found = True 
            else:
                current = current.getNext()

        if found == True and previous == None:
            self.head = current.getNext()

        if found == True and previous != None:
            previous.setNext(current.getNext())