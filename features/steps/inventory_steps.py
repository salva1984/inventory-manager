from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from behave import given, when, then

from inventory_service import add_product, remove_product
from product import build_product
from storage import load_products, save_products


def make_inventory(context) -> list[dict]:
    if not hasattr(context, "temp_dir"):
        context.temp_dir = TemporaryDirectory()
        context.storage_path = Path(context.temp_dir.name) / "inventory.json"
        context.products = load_products(context.storage_path)
    return context.products


def persist(context) -> None:
    save_products(context.products, context.storage_path)


@given('an inventory with a product "{product_id}"')
def step_inventory_with_product(context, product_id):
    context.products = add_product(
        make_inventory(context),
        build_product(
            product_id,
            "Sample product",
            "Sample description",
            10,
            2.5,
            "General",
        ),
    )
    persist(context)


@when('I remove the product "{product_id}"')
def step_remove_product(context, product_id):
    context.products = remove_product(context.products, product_id)
    persist(context)


@then("the inventory should contain {expected_count:d} products")
def step_inventory_count(context, expected_count):
    assert len(make_inventory(context)) == expected_count