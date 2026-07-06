from __future__ import annotations

from copy import deepcopy
from typing import Any

from product import normalize_product

def list_products(products: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return deepcopy(products)

def find_product(products: list[dict[str, Any]], product_id: str) -> dict[str, Any] | None:
    for product in products:
        if product["id"] == product_id:
            return product
    return None
    
def add_product(products: list[dict[str, Any]], product: dict[str, Any]) -> list[dict[str, Any]]:
    normalized = normalize_product(product)
    if find_product(products, normalized["id"]) is not None:
        raise ValueError(f"Product '{normalized['id']}' already exists")

    updated_products = deepcopy(products)
    updated_products.append(normalized)
    return updated_products

def remove_product(products: list[dict[str, Any]], product_id: str) -> list[dict[str, Any]]:
    if find_product(products, product_id) is None:
        raise ValueError(f"Product '{product_id}' not found")

    return [product for product in products if product["id"] != product_id]