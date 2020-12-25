  Feature: Looking for new items in a store

    @TCID-1
    Scenario: Doing step by step

      Given TCID-1: user goes to 'url' page
      When TCID-1: user enters any 'item' in search bar
      And TCID-1: clicks on search button
      Then TCID-1: verify page title contains 'Apple iPhone XS Max, 64GB, Gold - Fully Unlocked (Renewed)' the search term

