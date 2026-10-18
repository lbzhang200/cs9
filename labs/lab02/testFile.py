from Beverage import Beverage
from Coffee import Coffee
from DrinkOrder import DrinkOrder
from FruitJuice import FruitJuice


# for beverages

def test_beverage_constructor_and_getters():
    b = Beverage(12, 2.25)
    assert b.getOunces() == 12
    assert b.getPrice() == 2.25


def test_beverage_update_ounces():
    b = Beverage(12, 2.25)
    b.updateOunces(10)
    assert b.getOunces() == 10
    assert b.getPrice() == 2.25


def test_beverage_update_price():
    b = Beverage(12, 2.25)
    b.updatePrice(3.25)
    assert b.getOunces() == 12
    assert b.getPrice() == 3.25


def test_beverage_getInfo():
    assert Beverage(12, 2.25).getInfo() == "12 oz, $2.25"
    assert Beverage(20, 3.25).getInfo() == "20 oz, $3.25"
    assert Beverage(10, 1.5).getInfo() == "10 oz, $1.50"
    assert Beverage(32, 12.0).getInfo() == "32 oz, $12.00"


def test_beverage_getInfo_after_updates():
    b = Beverage(12, 2.25)
    b.updateOunces(10)
    b.updatePrice(3.25)
    assert b.getInfo() == "10 oz, $3.25"


# for coffee

def test_coffee_inherits_getters():
    c = Coffee(12, 2.25, "Americano")
    assert c.getOunces() == 12
    assert c.getPrice() == 2.25
    assert isinstance(c, Beverage)


def test_coffee_getInfo():
    assert Coffee(12, 4.25, "Latte").getInfo() == "Latte Coffee, 12 oz, $4.25"
    assert Coffee(15, 3.25, "Cortado").getInfo() == "Cortado Coffee, 15 oz, $3.25"
    assert Coffee(8, 3.0, "Mocha").getInfo() == "Mocha Coffee, 8 oz, $3.00"


def test_coffee_getInfo_after_updates():
    c = Coffee(12, 2.25, "Americano")
    c.updateOunces(15)
    c.updatePrice(3.25)
    assert c.getOunces() == 15
    assert c.getPrice() == 3.25
    assert c.getInfo() == "Americano Coffee, 15 oz, $3.25"


# for fruit juice

def test_fruitjuice_inherits_getters():
    f = FruitJuice(12, 2.25, ["Mango"])
    assert f.getOunces() == 12
    assert f.getPrice() == 2.25
    assert isinstance(f, Beverage)


def test_fruitjuice_getInfo_one_fruit():
    assert FruitJuice(15, 3.25, ["Orange"]).getInfo() == "Orange Juice, 15 oz, $3.25"


def test_fruitjuice_getInfo_multiple_fruits():
    assert FruitJuice(12, 2.25, ["Strawberry", "Coconut"]).getInfo() == "Strawberry/Coconut Juice, 12 oz, $2.25"
    assert FruitJuice(24, 7.5, ["Kiwi", "Banana", "Lime"]).getInfo() == "Kiwi/Banana/Lime Juice, 24 oz, $7.50"


def test_fruitjuice_after_updates():
    f = FruitJuice(12, 2.25, ["Mango", "Apple"])
    f.updateOunces(15)
    f.updatePrice(3.25)
    assert f.getOunces() == 15
    assert f.getPrice() == 3.25
    assert f.getInfo() == "Mango/Apple Juice, 15 oz, $3.25"


# for drink order

def test_drinkorder_empty():
    order = DrinkOrder()
    assert order.drinks == []
    assert order.getTotalOrder() == "Order Items:\nTotal Price: $0.00"


def test_drinkorder_addBeverage_order_preserved():
    order = DrinkOrder()
    c = Coffee(10, 3.25, "Flat White")
    j = FruitJuice(12, 5.0, ["Grape"])
    order.addBeverage(c)
    assert len(order.drinks) == 1
    assert order.drinks[-1] is c
    order.addBeverage(j)
    assert len(order.drinks) == 2
    assert order.drinks[0] is c
    assert order.drinks[1] is j


def test_drinkorder_single_item():
    order = DrinkOrder()
    order.addBeverage(Coffee(4, 2.5, "Macchiato"))
    assert order.getTotalOrder() == (
        "Order Items:\n"
        "* Macchiato Coffee, 4 oz, $2.50\n"
        "Total Price: $2.50"
    )


def test_drinkorder_multiple_items():
    order = DrinkOrder()
    order.addBeverage(FruitJuice(20, 6.25, ["Watermelon", "Lime"]))
    order.addBeverage(Coffee(16, 4.0, "Cold Brew"))
    order.addBeverage(FruitJuice(8, 2.5, ["Lemon"]))
    assert order.getTotalOrder() == (
        "Order Items:\n"
        "* Watermelon/Lime Juice, 20 oz, $6.25\n"
        "* Cold Brew Coffee, 16 oz, $4.00\n"
        "* Lemon Juice, 8 oz, $2.50\n"
        "Total Price: $12.75"
    )


def test_drinkorder_reflects_price_update():
    c = Coffee(8, 3.0, "Latte")
    order = DrinkOrder()
    order.addBeverage(c)
    c.updatePrice(4.5)
    assert order.getTotalOrder() == (
        "Order Items:\n"
        "* Latte Coffee, 8 oz, $4.50\n"
        "Total Price: $4.50"
    )


def test_drinkorder_same_beverage_twice():
    c = Coffee(8, 3.0, "Espresso")
    order = DrinkOrder()
    order.addBeverage(c)
    order.addBeverage(c)
    assert order.getTotalOrder() == (
        "Order Items:\n"
        "* Espresso Coffee, 8 oz, $3.00\n"
        "* Espresso Coffee, 8 oz, $3.00\n"
        "Total Price: $6.00"
    )