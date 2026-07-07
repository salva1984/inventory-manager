from __future__ import annotations

from behave import given, when, then
from inventory_service import add_product
from product import build_product


@given("the inventory is empty")
def step_given_inventory_is_empty(context) -> None:
    """
    Step definition for Gherkin: 'Given the inventory is empty'.
    Initializes context.products as an empty list.
    """
    context.products = []


@when('the user adds a product "{product_name}"')
def step_when_user_adds_product(context, product_name: str) -> None:
    """
    Step definition for Gherkin: 'When the user adds a product "{product_name}"'.
    Adds a product with default attributes to the inventory using the service.
    """
    # Build product with a generated ID and default quantity/price
    product_id = f"P{len(context.products) + 1:03d}"
    product = build_product(
        product_id=product_id,
        name=product_name,
        description=product_name,
        quantity=1,
        price=10.00,
        category="General"
    )
    context.products = add_product(context.products, product)


@then('the inventory should contain "{product_name}"')
def step_then_inventory_should_contain(context, product_name: str) -> None:
    """
    Step definition for Gherkin: 'Then the inventory should contain "{product_name}"'.
    Verifies that a product with the given name exists in the inventory.
    """
    found = any(p["name"] == product_name for p in context.products)
    assert found, f"Expected product '{product_name}' to be in the inventory, but it was not."
