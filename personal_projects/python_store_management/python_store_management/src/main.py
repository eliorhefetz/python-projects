from product import Product, DiscountProduct
from store_manager import StoreManager
from storage import save_products, load_products
from utils import read_non_empty_text, read_int, read_float


def show_products(manager):
    if not manager.products:
        print("No products found.")
        return
    for product in manager.products:
        print(
            f"ID: {product.product_id} | Name: {product.name} | "
            f"Category: {product.category} | Price: {product.get_price():.2f} | Stock: {product.stock}"
        )


def main():
    manager = StoreManager()
    while True:
        print("\nStore Management")
        print("1. Add regular product")
        print("2. Add discount product")
        print("3. Update stock")
        print("4. Buy product")
        print("5. Show products")
        print("6. Show discounted products")
        print("7. Show inventory value")
        print("8. Save")
        print("9. Load")
        print("10. Exit")

        choice = input("Choose an option (1-10): ").strip()
        try:
            if choice == "1":
                manager.add_product(Product(
                    read_non_empty_text("Product ID: "),
                    read_non_empty_text("Name: "),
                    read_non_empty_text("Category: "),
                    read_float("Price: ", 0),
                    read_int("Stock: ", 0),
                ))
                print("Product added successfully.")
            elif choice == "2":
                manager.add_product(DiscountProduct(
                    read_non_empty_text("Product ID: "),
                    read_non_empty_text("Name: "),
                    read_non_empty_text("Category: "),
                    read_float("Price: ", 0),
                    read_int("Stock: ", 0),
                    read_float("Discount percentage: ", 0),
                ))
                print("Discount product added successfully.")
            elif choice == "3":
                manager.update_stock(read_non_empty_text("Product ID: "), read_int("Amount to add/remove: "))
                print("Stock updated successfully.")
            elif choice == "4":
                change = manager.buy_product(
                    read_non_empty_text("Product ID: "),
                    read_int("Quantity: ", 1),
                    read_float("Money received: ", 0),
                )
                print(f"Purchase completed. Change: {change:.2f}")
            elif choice == "5":
                show_products(manager)
            elif choice == "6":
                products = manager.get_discounted_products()
                if not products:
                    print("No discounted products found.")
                else:
                    for product in products:
                        print(f"{product.name} | Discounted price: {product.get_price():.2f}")
            elif choice == "7":
                print(f"Total inventory value: {manager.get_total_inventory_value():.2f}")
            elif choice == "8":
                save_products("store_data.json", manager.products)
                print("Data saved successfully.")
            elif choice == "9":
                manager.products = load_products("store_data.json")
                print("Data loaded successfully.")
            elif choice == "10":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
