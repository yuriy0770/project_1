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

    @classmethod
    def new_product(cls, data: dict):
        if 'name' not in data or 'price' not in data or 'quantity' not in data:
            raise ValueError("Недостаточно параметров для создания продукта")

        return cls(data['name'], data.get('description', ''), float(data['price']), int(data['quantity']))

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value



class Category:
    name: str
    description: str
    products: list[str]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Нельзя добавить не продукт в категорию")

    @property
    def products(self):
        product_list = [f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт' for product in
                        self.__products]
        return '\n'.join(product_list)
