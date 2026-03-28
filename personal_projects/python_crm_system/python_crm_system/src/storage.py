import json
from pathlib import Path

from customer import Customer


def save_customers(file_path, customers):
    payload = [customer.to_dict() for customer in customers]
    Path(file_path).write_text(json.dumps(payload, indent=4), encoding="utf-8")


def load_customers(file_path):
    path = Path(file_path)
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [Customer.from_dict(item) for item in payload]
