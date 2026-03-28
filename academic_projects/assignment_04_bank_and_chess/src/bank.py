class BankAccount:
    def __init__(self, account_id, owner_name, balance):
        self.id = account_id
        self.owner_name = owner_name.strip()

        if self.id <= 0:
            raise ValueError("Account ID must be greater than 0.")
        if not self.owner_name:
            raise ValueError("Owner name cannot be empty.")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.balance = balance
        self.actions = {"Deposit": [], "Withdraw": []}

    def __repr__(self):
        return f"BankAccount(id={self.id}, owner_name='{self.owner_name}', balance={self.balance})"

    def Deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            return "Invalid amount"

        self.balance += amount
        self.actions["Deposit"].append(amount)
        return "Deposit completed"

    def Withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Not enough balance"

        self.balance -= amount
        self.actions["Withdraw"].append(amount)
        return "Withdraw completed"

    def totalActions(self):
        return self._sum_list(self.actions["Deposit"], 0) + self._sum_list(self.actions["Withdraw"], 0)

    def _sum_list(self, values, index):
        if index == len(values):
            return 0
        return values[index] + self._sum_list(values, index + 1)

    def allDeposits(self):
        deposits = self.actions["Deposit"][:]
        self._insertion_sort(deposits)
        return deposits

    def allWithdraws(self):
        withdraws = self.actions["Withdraw"][:]
        self._insertion_sort(withdraws)
        return withdraws

    def _insertion_sort(self, values):
        for i in range(1, len(values)):
            key = values[i]
            j = i - 1
            while j >= 0 and values[j] > key:
                values[j + 1] = values[j]
                j -= 1
            values[j + 1] = key


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name.strip()
        if not self.bank_name:
            raise ValueError("Bank name cannot be empty.")
        self.accounts = []

    def __repr__(self):
        return f"Bank(bank_name='{self.bank_name}', accounts={self.accounts})"

    def addAccount(self, account):
        for existing_account in self.accounts:
            if existing_account.id == account.id:
                raise ValueError(f"Account with ID {account.id} already exists.")

        self.accounts.append(account)
        self._sort_accounts_by_balance()

    def _sort_accounts_by_balance(self):
        for i in range(1, len(self.accounts)):
            key = self.accounts[i]
            j = i - 1
            while j >= 0 and self.accounts[j].balance > key.balance:
                self.accounts[j + 1] = self.accounts[j]
                j -= 1
            self.accounts[j + 1] = key

    def removeAccount(self, account_id):
        for index, account in enumerate(self.accounts):
            if account.id == account_id:
                del self.accounts[index]
                return "Account removed"
        return "Account not found"

    def totalBalance(self):
        return self._totalBalance_recursive(0)

    def _totalBalance_recursive(self, index):
        if index == len(self.accounts):
            return 0
        return self.accounts[index].balance + self._totalBalance_recursive(index + 1)

    def findAccount(self, account_id):
        return self._findAccount_recursive(account_id, 0)

    def _findAccount_recursive(self, account_id, index):
        if index == len(self.accounts):
            return "Account not found"
        if self.accounts[index].id == account_id:
            return self.accounts[index].owner_name, self.accounts[index].balance
        return self._findAccount_recursive(account_id, index + 1)


def run_bank_examples():
    account_1 = BankAccount(1, "Elior", 1000)
    account_2 = BankAccount(2, "Eli", 2500)
    account_3 = BankAccount(3, "Or", 1500)

    account_1.Deposit(300)
    account_1.Deposit(200)
    account_1.Withdraw(100)

    account_2.Deposit(500)
    account_2.Withdraw(200)

    print(account_1)
    print("Total actions:", account_1.totalActions())
    print("All deposits:", account_1.allDeposits())
    print("All withdraws:", account_1.allWithdraws())

    bank = Bank("Leumi")
    bank.addAccount(account_1)
    bank.addAccount(account_2)
    bank.addAccount(account_3)

    print(bank)
    print("Total balance:", bank.totalBalance())
    print("Find account 2:", bank.findAccount(2))
    print("Remove account 3:", bank.removeAccount(3))
    print("Remaining accounts:", bank.accounts)


if __name__ == "__main__":
    run_bank_examples()
