from crm_manager import CRMManager
from storage import save_customers, load_customers
from utils import read_non_empty_text, read_int


def show_customers(customers):
    if not customers:
        print("No customers found.")
        return
    for customer in customers:
        print(
            f"ID: {customer.customer_id} | Name: {customer.name} | Phone: {customer.phone} | "
            f"Email: {customer.email} | Status: {customer.status}"
        )


def main():
    manager = CRMManager()
    while True:
        print("\nCRM System")
        print("1. Add customer")
        print("2. Update customer")
        print("3. Remove customer")
        print("4. Search customers")
        print("5. Add note")
        print("6. Show customers")
        print("7. Save")
        print("8. Load")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()
        try:
            if choice == "1":
                manager.add_customer(
                    read_int("Customer ID: ", 1),
                    read_non_empty_text("Name: "),
                    read_non_empty_text("Phone: "),
                    read_non_empty_text("Email: "),
                    read_non_empty_text("Status (new / active / inactive / lead): "),
                )
                print("Customer added successfully.")
            elif choice == "2":
                manager.update_customer(
                    read_int("Customer ID: ", 1),
                    read_non_empty_text("Name: "),
                    read_non_empty_text("Phone: "),
                    read_non_empty_text("Email: "),
                    read_non_empty_text("Status (new / active / inactive / lead): "),
                )
                print("Customer updated successfully.")
            elif choice == "3":
                manager.remove_customer(read_int("Customer ID: ", 1))
                print("Customer removed successfully.")
            elif choice == "4":
                keyword = read_non_empty_text("Keyword: ")
                show_customers(manager.search_customers(keyword))
            elif choice == "5":
                manager.add_note_to_customer(read_int("Customer ID: ", 1), read_non_empty_text("Note: "))
                print("Note added successfully.")
            elif choice == "6":
                show_customers(manager.customers)
            elif choice == "7":
                save_customers("crm_data.json", manager.customers)
                print("Data saved successfully.")
            elif choice == "8":
                manager.customers = load_customers("crm_data.json")
                print("Data loaded successfully.")
            elif choice == "9":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
