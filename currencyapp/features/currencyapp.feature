Feature: showing off behave

  Scenario: Successful transaction
    Given a user
    When I log in with username admin and password admin
    Then I go to the /currencyapp/ page
    When I fill the form
    Then I see 2300.000 in the result section the results


  Scenario: Unsuccessful transaction
    Given a user
    When I log in with username admin and password admin
    Then I go to the /currencyapp/ page
    When I fill the form with the same sell and buy currencies
    Then I see a warning Sell and buy currencies must be different