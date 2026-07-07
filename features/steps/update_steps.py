from __future__ import annotations

from behave import then, when

from inventory_service import find_product, update_product_quantity


@when('the user updates product "{product_id}" to quantity "{quantity}"')
def step_when_user_updates_quantity(context, product_id, quantity):
    context.products = update_product_quantity(context.products, product_id, int(quantity))


@then('the inventory should show product "{product_id}" with quantity "{quantity}"')
def step_then_inventory_should_show_quantity(context, product_id, quantity):
    product = find_product(context.products, product_id)
    assert product is not None, f"Product '{product_id}' not found"
    assert product["quantity"] == int(quantity), (
        f"Expected quantity {quantity} but got {product['quantity']}"
    )
