from __future__ import annotations

from copy import deepcopy
from typing import Any

from product import normalize_product

def list_products(products: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return deepcopy(products)