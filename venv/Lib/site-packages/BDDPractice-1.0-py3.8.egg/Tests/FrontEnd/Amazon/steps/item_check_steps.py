from selenium import webdriver
from behave import step, given, when, then
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs.locatorsconfig import LOCATORS
from BDDCommon.CommonConfigs.locatorsconfig import HOME




@given("TCID-1: user goes to '{url}' page")
def TCID_1_user_goes_to_home_page(context, url):

    print("Navigating to the page: {}".format(url))
    webcommon.go_to(context, url)

    print("Contains url: {}".format(url))
    webcommon.url_contains(context, url)

@when("TCID-1: user enters any 'item' in search bar")
def TCID_1_user_enters_any_item_in_search_bar(context):

    search_bar_locator = LOCATORS['search bar']
    search_bar_locator_type = search_bar_locator['type']
    search_bar_locator_text = search_bar_locator['locator']

    webcommon.type_into_element(context, "iphone", search_bar_locator_type, search_bar_locator_text)


@when("TCID-1: clicks on search button")
def TCID_1_clicks_on_search_button(context):

    search_button = HOME['button']
    search_button_type = search_button['type']
    search_button_text = search_button['locator']
    webcommon.click(context,  search_button_type, search_button_text)



@then("TCID-1: verify page title contains '{expected_text}' the search term")
def TCID_1_verify_page_title_contains_the_search_term(context, expected_text):


    search_result = HOME['search result']
    search_result_type = search_result['type']
    search_result_text = search_result['locator']
    webcommon.element_contains_text(context, expected_text, search_result_type, search_result_text)
