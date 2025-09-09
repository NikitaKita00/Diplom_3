import pytest
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    @pytest.mark.parametrize(
        "name",
        ["black bun", "white bun", "red bun", "", "special bun"],
    )
    def test_get_name(self, name):
        bun = Bun(name, 123.45)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [100.0, 200.0, 300.0, 0.0, 999.99],
    )
    def test_get_price(self, price):
        bun = Bun("test bun", price)
        assert bun.get_price() == price

    def test_bun_name_type(self):
        bun = Bun("test", 100)
        assert isinstance(bun.get_name(), str)

    def test_bun_price_type(self):
        bun = Bun("test", 100.5)
        assert isinstance(bun.get_price(), float)
