Feature: Verify the Target Circle Page

  Scenario: Verify the number of benefit cells on the Target Circle page
    Given I open the Target Circle page
    Then I should see exactly 10 benefit cells
