import pytest

from src.categories import Product, Category
from .config import product, description, price, quantity, category_name, category_description


def test_product_init(product, description, price, quantity):
    product_obj = Product(product, description, price, quantity)
    assert product_obj.name == product
    assert product_obj.description == description
    assert product_obj.price == price
    assert product_obj.quantity == quantity


def test_category_init(category_name, category_description):
    products = []
    category_obj = Category(category_name, category_description, products)
    assert category_obj.name == category_name
    assert category_obj.description == category_description
    assert len(category_obj.products) == 0


def test_category_count():
    Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [])
    assert Category.category_count == 2


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



