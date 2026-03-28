class Customer:
    def __init__(self, customer_id, name, phone, email, status="new"):
        self.customer_id = customer_id
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip()
        self.status = status.strip().lower()
        self.notes = []
        if self.customer_id <= 0:
            raise ValueError("Customer ID must be greater than 0.")
        if not self.name:
            raise ValueError("Customer name cannot be empty.")
        if not self.phone:
            raise ValueError("Phone cannot be empty.")
        if not self.email:
            raise ValueError("Email cannot be empty.")
        if self.status not in {"new", "active", "inactive", "lead"}:
            raise ValueError("Status must be new, active, inactive, or lead.")

    def add_note(self, note):
        cleaned_note = note.strip()
        if not cleaned_note:
            raise ValueError("Note cannot be empty.")
        self.notes.append(cleaned_note)

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "status": self.status,
            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data):
        customer = cls(data["customer_id"], data["name"], data["phone"], data["email"], data["status"])
        customer.notes = data.get("notes", [])
        return customer
