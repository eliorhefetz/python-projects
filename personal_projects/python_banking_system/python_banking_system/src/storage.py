import json
from pathlib import Path

from account import BankAccount


def save_accounts(file_path, bank_name, accounts):
    payload = {"bank_name": bank_name, "accounts": [account.to_dict() for account in accounts]}
    Path(file_path).write_text(json.dumps(payload, indent=4), encoding="utf-8")


def load_accounts(file_path):
    path = Path(file_path)
    if not path.exists():
        return "My Bank", []
    payload = json.loads(path.read_text(encoding="utf-8"))
    accounts = [BankAccount.from_dict(item) for item in payload.get("accounts", [])]
    return payload.get("bank_name", "My Bank"), accounts
