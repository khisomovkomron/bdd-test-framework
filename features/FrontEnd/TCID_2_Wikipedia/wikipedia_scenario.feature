  Feature: Checking for url

    @TCID-2
    Scenario: User passes to url and searches for page

      Given TCID-2: user goes to 'https://www.wikipedia.org/' page
      When TCID-2: user enters term 'selenium webdriver'
      And TCID-2: clicks on search button
      And TCID-2: clicks on search result Selenium (software)
      Then TCID-2: verifies url ends with 'Selenium_(software)'
