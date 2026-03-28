class BankAccount:
    def __init__(self, account_id, owner_name, balance=0):
        self.account_id = account_id
        self.owner_name = owner_name.strip()
        self.balance = balance
        self.transactions = []
        if self.account_id <= 0:
            raise ValueError("Account ID must be greater than 0.")
        if not self.owner_name:
            raise ValueError("Owner name cannot be empty.")
        if self.balance < 0:
            raise ValueError("Balance cannot be negative.")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        self.transactions.append(f"Withdraw: {amount}")

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "owner_name": self.owner_name,
            "balance": self.balance,
            "transactions": self.transactions,
        }

    @classmethod
    def from_dict(cls, data):
        account = cls(data["account_id"], data["owner_name"], data["balance"])
        account.transactions = data.get("transactions", [])
        return account
