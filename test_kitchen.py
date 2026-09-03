# test_kitchen.py
from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)

def test_multiplication_by_two():
    flour = Quantity(200)
    assert flour.times(2).amount == 400

def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400

def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)

def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")

def grams(amount):
    return Quantity(amount, "g")

def ounces(amount):
    return Quantity(amount, "oz")

def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)