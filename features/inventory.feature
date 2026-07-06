Feature: Inventory management

	Scenario: Calculate the total value of the inventory
		Given the inventory contains products:
			| ID   | Product | Quantity | Price |
			| P001 | Coffee  | 10       | 5.00  |
			| P002 | Sugar   | 4        | 2.50  |
		When the user requests the total inventory value
		Then the total value should be 60.00
