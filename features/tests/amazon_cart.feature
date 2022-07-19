# Created by v33ja at 7/16/2022
Feature: Amazon Cart Tests

  Scenario: # User can verify their empty Amazon Cart
    Given Open Amazon page
    When Click on cart icon
    Then Results for cart shown