from customer import Customer


class CRMManager:
    def __init__(self):
        self.customers = []

    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def add_customer(self, customer_id, name, phone, email, status="new"):
        if self.find_customer_by_id(customer_id) is not None:
            raise ValueError("Customer ID already exists.")
        self.customers.append(Customer(customer_id, name, phone, email, status))

    def update_customer(self, customer_id, name, phone, email, status):
        customer = self.find_customer_by_id(customer_id)
        if customer is None:
            raise ValueError("Customer not found.")
        updated = Customer(customer_id, name, phone, email, status)
        updated.notes = customer.notes[:]
        index = self.customers.index(customer)
        self.customers[index] = updated

    def remove_customer(self, customer_id):
        customer = self.find_customer_by_id(customer_id)
        if customer is None:
            raise ValueError("Customer not found.")
        self.customers.remove(customer)

    def search_customers(self, keyword):
        cleaned_keyword = keyword.strip().lower()
        return [
            customer for customer in self.customers
            if cleaned_keyword in customer.name.lower()
            or cleaned_keyword in customer.phone.lower()
            or cleaned_keyword in customer.email.lower()
        ]

    def add_note_to_customer(self, customer_id, note):
        customer = self.find_customer_by_id(customer_id)
        if customer is None:
            raise ValueError("Customer not found.")
        customer.add_note(note)
