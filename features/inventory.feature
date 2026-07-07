Feature: Inventory management

Scenario: Remove a product from the inventory
    Given an inventory with a product "D400"
    When I remove the product "D400"
    Then the inventory should contain 0 products

Scenario: Calculate the total value of the inventory
		Given the inventory contains products:
			| ID   | Product | Quantity | Price |
			| P001 | Coffee  | 10       | 5.00  |
			| P002 | Sugar   | 4        | 2.50  |
		When the user requests the total inventory value
		Then the total value should be 60.00

	Scenario: Update the quantity of a product
		Given the inventory contains products:
			| ID   | Product | Quantity | Price |
			| P001 | Coffee  | 10       | 5.00  |
		When the user updates product "P001" to quantity "25"
		Then the inventory should show product "P001" with quantity "25"
