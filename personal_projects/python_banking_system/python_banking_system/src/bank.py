from account import BankAccount


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name.strip()
        self.accounts = []
        if not self.bank_name:
            raise ValueError("Bank name cannot be empty.")

    def find_account(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def open_account(self, account_id, owner_name, balance=0):
        if self.find_account(account_id) is not None:
            raise ValueError("Account ID already exists.")
        self.accounts.append(BankAccount(account_id, owner_name, balance))
        self.sort_accounts_by_balance()

    def remove_account(self, account_id):
        account = self.find_account(account_id)
        if account is None:
            raise ValueError("Account not found.")
        self.accounts.remove(account)

    def transfer(self, sender_id, receiver_id, amount):
        sender = self.find_account(sender_id)
        receiver = self.find_account(receiver_id)
        if sender is None or receiver is None:
            raise ValueError("Both accounts must exist.")
        if sender.account_id == receiver.account_id:
            raise ValueError("Cannot transfer to the same account.")
        sender.withdraw(amount)
        receiver.deposit(amount)
        sender.transactions.append(f"Transfer to {receiver_id}: {amount}")
        receiver.transactions.append(f"Transfer from {sender_id}: {amount}")
        self.sort_accounts_by_balance()

    def sort_accounts_by_balance(self):
        self.accounts.sort(key=lambda account: account.balance)

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts)
