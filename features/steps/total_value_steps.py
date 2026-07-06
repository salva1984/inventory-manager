from __future__ import annotations

from behave import given, then, when

from inventory_service import get_total_value


@given("the inventory contains products:")
def step_given_inventory_contains_products(context) -> None:
	context.products = [
		{
			"id": row["ID"],
			"name": row["Product"],
			"description": row["Product"],
			"quantity": int(row["Quantity"]),
			"price": float(row["Price"]),
			"category": "General",
		}
		for row in context.table
	]


@when("the user requests the total inventory value")
def step_when_user_requests_total_inventory_value(context) -> None:
	context.total_value = get_total_value(context.products)


@then("the total value should be {expected_total:f}")
def step_then_total_value_should_be(context, expected_total: float) -> None:
	assert context.total_value == expected_total
