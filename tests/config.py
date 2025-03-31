import pytest

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

