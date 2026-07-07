from __future__ import annotations

from behave import when, then
from inventory_service import list_products


@when("the user lists all products")
def step_when_user_lists_all_products(context) -> None:
    """
    Step definition for Gherkin: 'When the user lists all products'.
    
    This step retrieves all products currently stored in the scenario's 
    context using `list_products` from the inventory service, formats the 
    list as a plain text string listing product names, and stores the formatted 
    output in `context.output` for assertion in the 'Then' steps.
    """
    # Use the inventory service to list products
    products = list_products(context.products)
    lines = ["Products:"]
    for p in products:
        lines.append(f"- {p['name']}")
    context.output = "\n".join(lines)


@then("the output should contain:")
def step_then_output_should_contain(context) -> None:
    """
    Step definition for Gherkin: 'Then the output should contain:'.
    
    This step verifies that the multiline text block (docstring) specified 
    in the Gherkin feature file is contained within the formatted output 
    saved in `context.output`.
    """
    expected_output = context.text.strip()
    actual_output = context.output.strip()
    assert expected_output in actual_output, (
        f"Expected output to contain:\n{expected_output}\nbut was:\n{actual_output}"
    )
