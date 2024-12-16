Feature: f1 function returns a sorted list of jobs

  Scenario: using f1 function on json data
    Given I have loaded json data
    When the f1 function is used
    Then the result should be sorted
