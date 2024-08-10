Feature: Verify Sign In Navigation

  Scenario: Navigate to Sign In page
    Given I open the Target website for sign in
    When I click on the Sign In button
    And I click on the Sign In link from the right side navigation menu
    Then I should see the Sign In form
