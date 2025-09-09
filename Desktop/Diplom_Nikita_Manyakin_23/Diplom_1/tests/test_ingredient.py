import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient, по одному тесту на метод"""

    @pytest.mark.parametrize(
        "name", ["hot sauce", "sour cream", "cutlet", "dinosaur", "test"]
    )
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 123.45)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [100.0, 200.0, 150.0, 250.0, 0.0])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "any", price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        "ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING, "UNKNOWN"]
    )
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "any", 123.45)
        assert ingredient.get_type() == ingredient_type

    def test_name_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", 100)
        assert isinstance(ingredient.get_name(), str)

    def test_price_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", 100.5)
        assert isinstance(ingredient.get_price(), float)

    def test_type_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", 100)
        assert isinstance(ingredient.get_type(), str)
