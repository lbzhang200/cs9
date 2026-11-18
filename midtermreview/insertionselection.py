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


#merge sort and quick sort 

#merge sort

#o(logn), subdivide until size == 1 

def mergesort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2


    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    mergesort(lefthalf) #sort the left half 
    mergesort(righthalf) #sort the right half 

    i = 0 #index for lefthalf sublist 
    j = 0 #index for righthalf sublist
    k = 0 #index for alist 


    while i < len(lefthalf) and j < len(righthalf): #compare both halves here 
        if lefthalf[i] <= righthalf[j]: #if first half index is less than 
            i = i + 1 #keep searching 
        else:
            alist[k] = righthalf[j]  
            j = j + 1
        k = k + 1 #actual index of alist, keep iterating until u gotta put something into it 


    #put the remaining lefthalf elements into alist 
    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i = i + 1
        k = k + 1


    #put the reamining righthalf elements into alist 
    while j < len(righthalf):
        alist[k] = righthalf[j]
        j = j + 1
        k = k + 1



#quick sort 
#pick a pivot (most of the time the first element), move everything smaller than the pivot to its left and everything bigger to its right 


def quicksort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

#helper function so u can pass in the first/last index 

def quickSortHelper(alist, first, last):
    if first < last: 

        splitpoint = partition(alist, first, last) 

        #recursively sort the left/right sublists 
        quickSortHelper(alist, first, splitpoint - 1) #left 
        quickSortHelper(alist, splitpoint + 1, last) #right 

def partition(alist, first, last):
    pivotvalue = alist[first] #choose first element as pivot 

    leftmark = first + 1
    rightmark = last 


    done = False 
    while not done:

        #keep going until we find left element > pivot 
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        #keep going until we find right element < pivot 
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        #check if were doing swapping left/right elements in correct side

        if rightmark < leftmark:
            done = True 
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp 




def quicksort(alist): 
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1 #looks for the left mark 
    rightmark = last #looks for the last mark 


    done = True 
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1


        if rightmark < leftmark:
            done = True 
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp 



#tracing 
def mergesort(alist): 
    if len(alist) > 1:
        mid = len(alist) // 2

    lefthalf = alist[:mid] #looking at the left half of the list 
    righthalf = alist[mid:] #looking at the right half of the list 

    mergesort(lefthalf)
    mergesort(righthalf)

    i = 0
    k = 0 
    j = 0 

    while i < len(lefthalf) and i < len(righthalf): #compare both halves here 
        if lefthalf[i] <= righthalf[i]: #if the left half is less than the right half 
            i += 1 #increment by one  
        else: #if its less 
            alist[k] = righthalf[j]  #addto the list 
            j += 1
        k += 1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i += 1
        k+= 1

    while j < len(righthalf):
        alist[j] = righthalf[j] 
        j += 1
        k += 1


    while i < len(lefthalf) and i < len(righthalf):
        if lefthalf[i] <= righthalf[i]:
            i += 1
        else:
            alist[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lasthalf):
        alist[k] = lefthalf[i] 
        j += 1
        k += 1

    while j < len(righthalf):
        alist[j] = righthalf[j] 
        j += 1
        k += 1


def quicksort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first  + 1
    rightmark = last 

    done = False 
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -=1 


    if rightmark < leftmark:
        done = True 
    else:
        temp = alist[leftmark]
        alist[leftmark] = alist[rightmark]
        alist[rightmark] = temp

def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last 

    done = False 
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -=1 

    if rightmark < leftmark:
        done = True 
    else:
        temp = alist[leftmark]
        alist[leftmark] = alist[rightmark]
        alist[rightmark] = temp 



