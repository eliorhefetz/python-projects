import unittest

from src.bank import Bank, BankAccount


class TestBank(unittest.TestCase):
    def test_total_actions_sums_deposits_and_withdraws(self):
        account = BankAccount(1, "Elior", 1000)
        account.Deposit(300)
        account.Deposit(200)
        account.Withdraw(100)

        self.assertEqual(account.totalActions(), 600)

    def test_add_account_sorts_by_balance(self):
        bank = Bank("Leumi")
        bank.addAccount(BankAccount(1, "Elior", 1000))
        bank.addAccount(BankAccount(2, "Eli", 2500))
        bank.addAccount(BankAccount(3, "Or", 1500))

        self.assertEqual([account.id for account in bank.accounts], [1, 3, 2])

    def test_find_account_returns_owner_and_balance(self):
        bank = Bank("Leumi")
        bank.addAccount(BankAccount(1, "Elior", 1000))

        self.assertEqual(bank.findAccount(1), ("Elior", 1000))


if __name__ == "__main__":
    unittest.main()
