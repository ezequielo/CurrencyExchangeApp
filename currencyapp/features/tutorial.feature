Feature: showing off behave

  Scenario: Successful transaction
    Given a user
    When I log in
    Then I go to the main page
    When I fill the form
    Then I see the results


  Scenario: Unsuccessful transaction
    Given a user
    When I log in
    Then I go to the main page
    When I fill the form with the same sell and buy currencies
    Then I see a warning