import pytest
from Best_Buy_Project import products


def test_creating_product():
    assert products.Product("MacBook Air M2", price=1450, quantity=100)


def test_creating_product_invalid_details():
    with pytest.raises(Exception, match="Either name,price or quantity of the product is wrong"):
        products.Product("", price="22", quantity=-5)


def test_product_become_inactive():
    mac = products.Product("MacBook Air M2", price=1450, quantity=0)
    assert products.Product.is_active(mac) is False


def test_buy_modifies_quantity():
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    products.Product.buy(mac, 100)
    assert mac.quantity == 0


def test_buy_too_much():
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(Exception, match=f"Only have {mac.quantity} in our inventory"):
        products.Product.buy(mac, quantity=150)

