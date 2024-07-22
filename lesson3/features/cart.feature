# Created by tameralkateeb at 7/17/24
Feature: Verify Cart Functionality


  Scenario: Verify "Your cart is empty" message is shown
    Given I open the Target website
    When I click on the Cart icon
    Then I should see the message "Your cart is empty"
