from Apartment import Apartment 

def mergesort(apartmentList):
    if len(apartmentList):
        mid = len(apartmentList) // 2
        left = apartmentList[:mid]
        right = apartmentList[mid:]


    mergesort(left)
    mergesort(right)

    i = j = k = 0
    #i is left, j is right, k is middle 

    while i < len(left) and j < len(right):
        if left[i] < right[j] or left[i] == right[j]:
            apartmentList[k] = left[i] 
            i += 1
        else:
            apartmentList[k] = right[j] 
            j += 1
        k += 1 

    while i < len(left):
        apartmentList[k] = left[i] 
        i += 1
        k += 1

    while j < len(right): 
        apartmentList[j] = right[j] 
        j += 1
        k += 1


def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList) - 1):
        if apartmentList[i] > apartmentList[i + 1]:
            return False 
    return True 

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget): 
    mergesort(apartmentList)
    affordable = []

    for apartment in apartmentList:
        if apartment.getRent() <= budget: 
            affordable.append(apartment.getDetails())
    return "\n".join(affordable)
    
