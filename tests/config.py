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
def category_str():
    return Category("Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    ["iphone", "Smart"])

@pytest.fixture()
def product_str():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture()
def product_str2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)