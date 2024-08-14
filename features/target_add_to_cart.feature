Feature: Add a product to the cart on Target

  Scenario: Add a product to the cart and verify it's added
    Given I open the Target website
    When I search for a product
    And I add the first product to the cart
    Then I should see the product in the cart
