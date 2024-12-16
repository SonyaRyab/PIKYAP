Feature: Unique iterator produces unique elements
  As a user i want my parsed data to not contain
  duplicates

  Scenario: Iterating over a list
    Given I have a sorted list of integers
    When Unique iterates over it
    Then Iterator returns only unique integers
