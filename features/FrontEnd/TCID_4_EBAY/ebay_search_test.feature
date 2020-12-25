Feature: Asserting quantity of items during search

  @TCID-4
  Scenario: Checking category quantity to all category quantity

    Given TCID-4: go to "https://ebay.com/" page
      And TCID-4: search for "wooden spoon"
      And TCID-4: save the total number of result
    When TCID-4: navigate back to previous research result page
    Then TCID-4: navigate back to home page
#    When TCID-4: click on link ALL under the categories on the left menu

#    Then TCID-4: verify that number of results is bigger than the number in step 4

#      And TCID-4: Verify that wooden spoon is still displayed in the search box

#      And TCID-4:verify that search box is blank
