Feature: Checking for urls for every item in search list

  # TCID = Test Case ID
  @TCID-3
  Scenario: Search for one of the strings in list

    Given TCID-3: user goes to 'https://www.google.com/' page
    And TCID-3: search for one of the strings the list item given below
#    And TCID-3: in the results pages, capture the url right above the first result
#    When TCID-3: click on the first result
#    Then TCID-3: verify that url is equal to the value from the step 4
##    And TCID-3: navigate back
#    And TCID-3: repeat the same steps for all search items in the list
#
#    Examples:
#              |item                           |
#              |Java                           |
#              |cucumber bdd                   |
#              |selenium web browser automation|
