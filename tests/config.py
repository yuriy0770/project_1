import pytest

from src.categories import Category, Product


@pytest.fixture(scope="session")
def product():
    return "Товар"


@pytest.fixture(scope="session")
def description():
    return "Описание товара"


@pytest.fixture(scope="session")
def price():
    return 100.0


@pytest.fixture(scope="session")
def quantity():
    return 10


@pytest.fixture(scope="session")
def category_name():
    return "Категория"


@pytest.fixture(scope="session")
def category_description():
    return "Описание категории"


@pytest.fixture()
def product_str():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product_str2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category():
    products = [
        Product.new_product({"name": "Продукт 1", "price": 100.0, "quantity": 5}),
        Product.new_product({"name": "Продукт 2", "price": 200.0, "quantity": 10})
    ]
    return Category("Категория", "Описание категории", products)