from product import DiscountProduct


class StoreManager:
    def __init__(self):
        self.products = []

    def find_product(self, product_id):
        cleaned_product_id = product_id.strip()
        for product in self.products:
            if product.product_id == cleaned_product_id:
                return product
        return None

    def add_product(self, product):
        if self.find_product(product.product_id) is not None:
            raise ValueError("Product ID already exists.")
        self.products.append(product)

    def update_stock(self, product_id, amount):
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product not found.")
        if product.stock + amount < 0:
            raise ValueError("Stock cannot become negative.")
        product.stock += amount

    def buy_product(self, product_id, quantity, money):
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product not found.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if money < 0:
            raise ValueError("Money cannot be negative.")
        if product.stock < quantity:
            raise ValueError("Not enough stock.")
        total_cost = product.get_price() * quantity
        if money < total_cost:
            raise ValueError("Not enough money.")
        product.stock -= quantity
        return money - total_cost

    def get_discounted_products(self):
        return [product for product in self.products if isinstance(product, DiscountProduct)]

    def get_total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.get_price() * product.stock
        return total
