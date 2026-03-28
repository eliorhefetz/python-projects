from bank import Bank
from storage import save_accounts, load_accounts
from utils import read_non_empty_text, read_int, read_float


def show_accounts(bank):
    if not bank.accounts:
        print("No accounts found.")
        return
    for account in bank.accounts:
        print(f"ID: {account.account_id} | Owner: {account.owner_name} | Balance: {account.balance:.2f}")


def show_transactions(bank, account_id):
    account = bank.find_account(account_id)
    if account is None:
        print("Account not found.")
        return
    if not account.transactions:
        print("No transactions found.")
        return
    for transaction in account.transactions:
        print(transaction)


def main():
    bank = Bank("My Bank")
    while True:
        print("\nBanking System")
        print("1. Open account")
        print("2. Remove account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Show accounts")
        print("7. Show transactions")
        print("8. Show total balance")
        print("9. Save")
        print("10. Load")
        print("11. Exit")

        choice = input("Choose an option (1-11): ").strip()
        try:
            if choice == "1":
                bank.open_account(
                    read_int("Account ID: ", 1),
                    read_non_empty_text("Owner name: "),
                    read_float("Initial balance: ", 0),
                )
                print("Account opened successfully.")
            elif choice == "2":
                bank.remove_account(read_int("Account ID: ", 1))
                print("Account removed successfully.")
            elif choice == "3":
                account = bank.find_account(read_int("Account ID: ", 1))
                if account is None:
                    print("Account not found.")
                else:
                    account.deposit(read_float("Deposit amount: ", 0.01))
                    bank.sort_accounts_by_balance()
                    print("Deposit completed.")
            elif choice == "4":
                account = bank.find_account(read_int("Account ID: ", 1))
                if account is None:
                    print("Account not found.")
                else:
                    account.withdraw(read_float("Withdraw amount: ", 0.01))
                    bank.sort_accounts_by_balance()
                    print("Withdraw completed.")
            elif choice == "5":
                bank.transfer(
                    read_int("Sender account ID: ", 1),
                    read_int("Receiver account ID: ", 1),
                    read_float("Transfer amount: ", 0.01),
                )
                print("Transfer completed.")
            elif choice == "6":
                show_accounts(bank)
            elif choice == "7":
                show_transactions(bank, read_int("Account ID: ", 1))
            elif choice == "8":
                print(f"Total bank balance: {bank.get_total_balance():.2f}")
            elif choice == "9":
                save_accounts("bank_data.json", bank.bank_name, bank.accounts)
                print("Data saved successfully.")
            elif choice == "10":
                bank_name, accounts = load_accounts("bank_data.json")
                bank = Bank(bank_name)
                bank.accounts = accounts
                bank.sort_accounts_by_balance()
                print("Data loaded successfully.")
            elif choice == "11":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
