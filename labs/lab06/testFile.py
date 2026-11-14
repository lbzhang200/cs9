from Apartment import Apartment
from lab06 import *


def test_getters():
    a = Apartment(1204, 200, "bad")
    assert a.getRent() == 1204
    assert a.getMetersFromUCSB() == 200
    assert a.getCondition() == "bad"


def test_getApartmentDetails():
    a = Apartment(1204, 200, "bad")
    assert a.getApartmentDetails() == \
        "(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad"


def test_lt_by_rent():
    assert Apartment(900, 500, "bad") < Apartment(950, 100, "excellent")
    assert not (Apartment(950, 100, "excellent") < Apartment(900, 500, "bad"))


def test_lt_by_distance():
    assert Apartment(950, 190, "bad") < Apartment(950, 215, "excellent")


def test_lt_by_condition():
    assert Apartment(950, 215, "excellent") < Apartment(950, 215, "average")
    assert Apartment(950, 215, "average") < Apartment(950, 215, "bad")


def test_gt():
    assert Apartment(1115, 215, "bad") > Apartment(950, 215, "average")
    assert Apartment(950, 215, "bad") > Apartment(950, 215, "excellent")
    assert not (Apartment(500, 250, "bad") > Apartment(900, 190, "excellent"))


def test_eq():
    assert Apartment(950, 215, "average") == Apartment(950, 215, "average")
    assert not (Apartment(950, 215, "average") == Apartment(950, 215, "bad"))
    assert not (Apartment(950, 215, "average") == Apartment(951, 215, "average"))


def test_ensureSortedAscending():
    assert ensureSortedAscending([]) == True
    assert ensureSortedAscending([Apartment(1, 1, "bad")]) == True
    assert ensureSortedAscending([Apartment(500, 250, "bad"),
                                  Apartment(900, 190, "excellent")]) == True
    assert ensureSortedAscending([Apartment(900, 190, "excellent"),
                                  Apartment(500, 250, "bad")]) == False
    # duplicates are still sorted
    assert ensureSortedAscending([Apartment(500, 250, "bad"),
                                  Apartment(500, 250, "bad")]) == True


def test_mergesort():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    assert apartmentList == [a5, a4, a3, a2, a1, a0]


def test_mergesort_edge_cases():
    empty = []
    mergesort(empty)
    assert empty == []
    single = [Apartment(1000, 100, "average")]
    mergesort(single)
    assert single[0].getRent() == 1000


def test_getBestAndWorstApartment():
    apartmentList = [Apartment(1200, 200, "average"),
                     Apartment(1200, 200, "excellent"),
                     Apartment(1000, 100, "average"),
                     Apartment(1000, 215, "excellent"),
                     Apartment(700, 315, "bad"),
                     Apartment(800, 250, "excellent")]
    assert getBestApartment(apartmentList) == \
        "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    assert getWorstApartment(apartmentList) == \
        "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"


def test_getBestAndWorst_single():
    apartmentList = [Apartment(800, 250, "excellent")]
    details = "(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent"
    assert getBestApartment(apartmentList) == details
    assert getWorstApartment(apartmentList) == details


def test_getAffordableApartments():
    apartmentList = [Apartment(1115, 215, "bad"),
                     Apartment(970, 215, "average"),
                     Apartment(950, 215, "average"),
                     Apartment(950, 190, "excellent"),
                     Apartment(900, 190, "excellent"),
                     Apartment(500, 250, "bad")]
    assert getAffordableApartments(apartmentList, 950) == \
        "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad\n" \
        "(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent\n" \
        "(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent\n" \
        "(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average"


def test_getAffordableApartments_none():
    apartmentList = [Apartment(1115, 215, "bad"), Apartment(970, 215, "average")]
    assert getAffordableApartments(apartmentList, 100) == ""


def test_getAffordableApartments_all():
    apartmentList = [Apartment(900, 190, "excellent"), Apartment(500, 250, "bad")]
    assert getAffordableApartments(apartmentList, 5000) == \
        "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad\n" \
        "(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent"