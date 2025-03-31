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


def test_category_products_init(category_name, category_description):
    products = [Product("Товар1", "", 0.0, 10), Product("Товар2", "", 0.0, 20)]
    category_obj = Category(category_name, category_description, products)
    assert len(category_obj.products) == 2


def test_category_product_count():
    products = [Product("", "", 0.0, 1), Product("", "", 0.0, 2)]
    category_obj = Category("Категория", "Описание", products)
    assert Category.product_count == 4
