"""JSON storage helpers for the inventory application."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_products(path: str | Path = "inventory.json") -> list[dict[str, Any]]:
    storage_path = Path(path)
    if not storage_path.exists():
        return []

    content = storage_path.read_text(encoding="utf-8").strip()
    if not content:
        return []

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("Inventory file must contain a list of products")
    return data


def save_products(products: list[dict[str, Any]], path: str | Path = "inventory.json") -> None:
    storage_path = Path(path)
    storage_path.parent.mkdir(parents=True, exist_ok=True)
    storage_path.write_text(
        json.dumps(products, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )