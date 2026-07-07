from __future__ import annotations

from copy import deepcopy
from typing import Any

from product import normalize_product

def list_products(products: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return deepcopy(products)

def add_product(products: list[dict[str, Any]], product: dict[str, Any]) -> list[dict[str, Any]]:
    normalized = normalize_product(product)
    if find_product(products, normalized["id"]) is not None:
        raise ValueError(f"Product '{normalized['id']}' already exists")

    updated_products = deepcopy(products)
    updated_products.append(normalized)
    return updated_products


def find_product(products: list[dict[str, Any]], product_id: str) -> dict[str, Any] | None:
    for product in products:
        if product["id"] == product_id:
            return deepcopy(product)
    return None


def update_product_quantity(products: list[dict[str, Any]], product_id: str, quantity: int) -> list[dict[str, Any]]:
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    if find_product(products, product_id) is None:
        raise ValueError(f"Product '{product_id}' was not found")

    updated_products = deepcopy(products)
    for product in updated_products:
        if product["id"] == product_id:
            product["quantity"] = quantity
            break
    return updated_products


def get_total_value(products: list[dict[str, Any]]) -> float:
    return sum(float(product["quantity"]) * float(product["price"]) for product in products)

