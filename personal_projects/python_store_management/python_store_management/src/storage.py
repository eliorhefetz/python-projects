import json
from pathlib import Path

from product import Product, DiscountProduct


def save_products(file_path, products):
    payload = [product.to_dict() for product in products]
    Path(file_path).write_text(json.dumps(payload, indent=4), encoding="utf-8")


def load_products(file_path):
    path = Path(file_path)
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    products = []
    for item in payload:
        if item["type"] == "discount_product":
            products.append(DiscountProduct.from_dict(item))
        else:
            products.append(Product.from_dict(item))
    return products
