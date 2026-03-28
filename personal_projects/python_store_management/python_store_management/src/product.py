class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id.strip()
        self.name = name.strip()
        self.category = category.strip()
        self.price = price
        self.stock = stock
        if not self.product_id:
            raise ValueError("Product ID cannot be empty.")
        if not self.name:
            raise ValueError("Product name cannot be empty.")
        if not self.category:
            raise ValueError("Category cannot be empty.")
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative.")

    def get_price(self):
        return self.price

    def to_dict(self):
        return {
            "type": "product",
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["product_id"], data["name"], data["category"], data["price"], data["stock"])


class DiscountProduct(Product):
    def __init__(self, product_id, name, category, price, stock, discount_percentage):
        super().__init__(product_id, name, category, price, stock)
        self.discount_percentage = discount_percentage
        if not 0 <= self.discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

    def get_price(self):
        return self.price * (1 - self.discount_percentage / 100)

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "discount_product"
        data["discount_percentage"] = self.discount_percentage
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["product_id"], data["name"], data["category"], data["price"], data["stock"], data["discount_percentage"])
