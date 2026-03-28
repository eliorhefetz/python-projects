from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    product_name: str
    department: str
    price: float

    def __post_init__(self) -> None:
        self.product_id = self.product_id.strip()
        self.product_name = self.product_name.strip()
        self.department = self.department.strip()

        if not self.product_id:
            raise ValueError("Product ID cannot be empty.")
        if not self.product_name:
            raise ValueError("Product name cannot be empty.")
        if not self.department:
            raise ValueError("Department cannot be empty.")
        if self.price < 0:
            raise ValueError("Price cannot be negative.")

    def GetPrice(self) -> float:
        return float(self.price)


@dataclass
class DiscountProduct(Product):
    discount_percentage: float

    def __post_init__(self) -> None:
        super().__post_init__()
        if not 0 <= self.discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

    def GetPrice(self) -> float:
        return self.price * (1 - self.discount_percentage / 100)


class Store:
    def __init__(self, store_name: str, owner_name: str) -> None:
        self.store_name = store_name.strip()
        self.owner_name = owner_name.strip()
        if not self.store_name:
            raise ValueError("Store name cannot be empty.")
        if not self.owner_name:
            raise ValueError("Owner name cannot be empty.")
        self.products: list[tuple[Product, int]] = []

    def __repr__(self) -> str:
        return f"Store(store_name='{self.store_name}', owner_name='{self.owner_name}', products_count={len(self.products)})"

    def AddProduct(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        for index, (existing_product, existing_quantity) in enumerate(self.products):
            if existing_product.product_id == product.product_id:
                self.products[index] = (existing_product, existing_quantity + quantity)
                return

        self.products.append((product, quantity))

    def TotalValue(self) -> float:
        total = 0.0
        for product, quantity in self.products:
            total += product.GetPrice() * quantity
        return total

    def GetDiscountProduct(self) -> list[str]:
        discount_products: list[str] = []
        for product, _ in self.products:
            if isinstance(product, DiscountProduct):
                discount_products.append(product.product_name)
        return discount_products

    def GetCheapestByDepartment(self, department: str):
        cleaned_department = department.strip()
        if not cleaned_department:
            raise ValueError("Department cannot be empty.")

        cheapest_product = None
        lowest_price = float("inf")

        for product, _ in self.products:
            if product.department.lower() == cleaned_department.lower():
                current_price = product.GetPrice()
                if current_price < lowest_price:
                    lowest_price = current_price
                    cheapest_product = product

        return cheapest_product

    def Buy(self, product_id: str, amount: int, money: float):
        cleaned_product_id = product_id.strip()

        if not cleaned_product_id:
            raise ValueError("Product ID cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if money < 0:
            raise ValueError("Money cannot be negative.")

        for index, (product, quantity) in enumerate(self.products):
            if product.product_id == cleaned_product_id:
                if quantity < amount:
                    return "Not enough stock"

                total_cost = product.GetPrice() * amount
                if money < total_cost:
                    return "Not enough money"

                remaining_quantity = quantity - amount
                if remaining_quantity == 0:
                    self.products.pop(index)
                else:
                    self.products[index] = (product, remaining_quantity)

                return money - total_cost

        return "Product not found"


def run_store_examples() -> None:
    my_store = Store("My Shop", "Elior")
    product_a = Product("A", "TestProduct", "General", 10)
    discount_product = DiscountProduct("B", "Discount TV", "Electronics", 1000, 20)

    my_store.AddProduct(product_a, 10)
    my_store.AddProduct(discount_product, 2)

    print(my_store)
    print("Total value:", my_store.TotalValue())
    print("Discount products:", my_store.GetDiscountProduct())
    print("Cheapest in General:", my_store.GetCheapestByDepartment("General"))

    print(f"Example 1 Result: {my_store.Buy('A', 20, 200)}")
    print(f"Example 2 Result: {my_store.Buy('A', 5, 30)}")
    print(f"Example 3 Result: {my_store.Buy('A', 2, 30)}")


if __name__ == "__main__":
    run_store_examples()
