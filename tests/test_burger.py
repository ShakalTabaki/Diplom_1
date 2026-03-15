from praktikum.burger import Burger
from unittest.mock import Mock


def test_burger_initial_state():
    burger = Burger()

    assert burger.bun is None
    assert burger.ingredients == []

def test_set_buns():
    burger = Burger()
    bun = Mock()

    burger.set_buns(bun)

    assert burger.bun == bun

def test_add_ingredient():
    burger = Burger()
    ingredient = Mock()

    burger.add_ingredient(ingredient)

    assert ingredient in burger.ingredients

def test_remove_ingredient():
    burger = Burger()
    ingredient1 = Mock()
    ingredient2 = Mock()

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient2]

def test_move_ingredient():
    burger = Burger()
    ingredient1 = Mock()
    ingredient2 = Mock()
    ingredient3 = Mock()

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

def test_get_price():
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = 100

    ingredient1 = Mock()
    ingredient1.get_price.return_value = 50

    ingredient2 = Mock()
    ingredient2.get_price.return_value = 30

    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    price = burger.get_price()

    assert price == 280

def test_get_receipt():
    burger = Burger()

    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    ingredient = Mock()
    ingredient.get_name.return_value = "sauce"
    ingredient.get_price.return_value = 50
    ingredient.get_type.return_value = "SAUCE"

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert "(==== black bun ====)" in receipt
    assert "= sauce sauce =" in receipt
    assert "Price: 250" in receipt