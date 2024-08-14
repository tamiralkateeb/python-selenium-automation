Feature: Target Product Search

Scenario Outline: Search for a product
  Given I open the Target homepage
  When I search for "<product>"
  Then I should see search results for <product>

Examples:
  | product       |
  | iPhone        |
  | Samsung TV    |
  | Nike Shoes    |

