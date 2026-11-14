class Apartment:
    CONDITION_RANK = {"excellent": 0, "average": 1, "bad": 2}

    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(
            self.rent, self.metersFromUCSB, self.condition)

    def _key(self):
        return (self.rent, self.metersFromUCSB, Apartment.CONDITION_RANK[self.condition])

    def __lt__(self, rhs):
        return self._key() < rhs._key()

    def __gt__(self, rhs):
        return self._key() > rhs._key()

    def __eq__(self, rhs):
        return self._key() == rhs._key()