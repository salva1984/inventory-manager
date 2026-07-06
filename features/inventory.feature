Feature: Inventory management

Scenario: Remove a product from the inventory
    Given an inventory with a product "D400"
    When I remove the product "D400"
    Then the inventory should contain 0 products