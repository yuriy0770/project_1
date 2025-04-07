import pytest

from src.categories import Product, Category
from .config import product, description, price, quantity, category_str, product_str, product_str2


def test_product_init(product, description, price, quantity):
    product_obj = Product(product, description, price, quantity)
    assert product_obj.name == product
    assert product_obj.description == description
    assert product_obj.price == price
    assert product_obj.quantity == quantity


def test_product_quantity(product):
    product_obj = Product(product, "", 0.0, 5)
    assert product_obj.quantity == 5


def test_category_product_count():
    assert Category.product_count == 0


def test_category_product_count_after_adding_product(product, description, price, quantity):
    category_obj = Category("Категория", "Описание категории", [])
    product_obj = Product(product, description, price, quantity)
    category_obj.add_product(product_obj)
    assert Category.product_count == 1


def test_category_product_count_after_adding_multiple_products(product, description, price, quantity):
    category_obj = Category("Категория", "Описание категории", [])
    product_obj1 = Product(product, description, price, quantity)
    product_obj2 = Product("Товар2", "", 0.0, 20)
    category_obj.add_product(product_obj1)
    category_obj.add_product(product_obj2)
    assert Category.product_count == 3


def test_adding_non_product_to_category():
    category_obj = Category("Категория", "Описание категории", [])
    with pytest.raises(ValueError):
        category_obj.add_product("Не продукт")


def test_cat_str(category_str):
    cat = category_str
    assert str(cat) == f"Смартфоны, количество продуктов: 2 шт."


def test_str(product_str):
    pro = product_str
    assert str(pro) == f"Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_add(product_str2, product_str):
    p1 = product_str2
    p2 = product_str
    assert p1 + p2 == 210000.0 * 8 + 31000.0 * 14
