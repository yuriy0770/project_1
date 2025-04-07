class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, data: dict):
        if "name" not in data or "price" not in data or "quantity" not in data:
            raise ValueError("Недостаточно параметров для создания продукта")

        return cls(
            data["name"],
            data.get("description", ""),
            float(data["price"]),
            int(data["quantity"]),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity


class Category:
    name: str
    description: str
    products: list[str]
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Нельзя добавить не продукт в категорию")
