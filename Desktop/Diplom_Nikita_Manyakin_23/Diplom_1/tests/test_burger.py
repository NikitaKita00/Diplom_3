import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from tests.helpers.mocks import create_mock_bun, create_mock_ingredient


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = create_mock_ingredient()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = create_mock_ingredient(name="ingredient1")
        mock_ingredient2 = create_mock_ingredient(name="ingredient2")
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient1

    def test_get_price(self):
        burger = Burger()
        mock_bun = create_mock_bun(price=150)
        mock_ingredient = create_mock_ingredient(price=75)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 375


def test_get_receipt():
    burger = Burger()

    bun = create_mock_bun(name="test bun", price=500)

    sauce = create_mock_ingredient(name="test sauce", price=100)
    sauce.type = "sauce"
    sauce.get_type.return_value = "sauce"

    filling = create_mock_ingredient(name="test filling", price=200)
    filling.type = "main"
    filling.get_type.return_value = "main"

    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    expected_receipt = (
        "(==== test bun ====)\n"
        "= sauce test sauce =\n"
        "= main test filling =\n"
        "(==== test bun ====)\n"
        "\n"
        "Price: 1300"
    )

    assert burger.get_receipt() == expected_receipt
