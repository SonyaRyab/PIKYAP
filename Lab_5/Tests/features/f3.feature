Feature: f3 function returns a list with all elements ending with a certain string

  Scenario: using f3 function on f2(f1(json data)
    Given I have loaded json data and used f1 and f2 functions consecutively
    When the f3 function is used
    Then the result should have all elements ending with a certain string
