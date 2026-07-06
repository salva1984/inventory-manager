"""Product helpers for the inventory application."""

from __future__ import annotations

from typing import Any


def normalize_product(product: dict[str, Any]) -> dict[str, Any]:
    normalized = {
        "id": str(product["id"]),
        "name": str(product["name"]),
        "description": str(product["description"]),
        "quantity": int(product["quantity"]),
        "price": float(product["price"]),
        "category": str(product["category"]),
    }

    if normalized["quantity"] < 0:
        raise ValueError("Quantity cannot be negative")

    if normalized["price"] < 0:
        raise ValueError("Price cannot be negative")

    return normalized


def build_product(
    product_id: str,
    name: str,
    description: str,
    quantity: int,
    price: float,
    category: str,
) -> dict[str, Any]:
    return normalize_product(
        {
            "id": product_id,
            "name": name,
            "description": description,
            "quantity": quantity,
            "price": price,
            "category": category,
        }
    )


def format_product(product: dict[str, Any]) -> str:
    return (
        f"{product['id']} | {product['name']} | {product['description']} | "
        f"qty={product['quantity']} | price={product['price']:.2f} | category={product['category']}"
    )