from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs.urlconfig import URLCONFIG
from BDDCommon.CommonConfigs.locatorsconfig import WIKI
from behave import given, when, then, step


@given("TCID-2: user goes to '{url}' page")
@step("TCID-2: user goes to '{url}' page")
def TCID_2_go_to_page(context, url):

    print("Navigating to the page: {}".format(url))
    webcommon.go_to(context, url)

@when("TCID-2: user enters term '{input_value}'")
def TCID_2_user_enters_text(context, input_value):

    search_bar = WIKI['search bar']
    search_bar_type = search_bar['type']
    search_bar_locator = search_bar['locator']

    webcommon.type_into_element(context, input_value, search_bar_type, search_bar_locator)

@when("TCID-2: clicks on search button")
def TCID_2_click_on_search_button_1(context):

    button = WIKI["button"]
    button_type = button['type']
    button_locator = button['locator']

    webcommon.click(context, button_type, button_locator)

@when("TCID-2: clicks on search result Selenium (software)")
def TCID_2_click_on_result(context):

    search_result = WIKI['search result']
    search_result_type = search_result['type']
    search_result_locator = search_result['locator']

    webcommon.click(context, search_result_type, search_result_locator)

@then("TCID-2: verifies url ends with '{text}'")
def TCID_2_verify_url_ends_with(context, text):

    webcommon.assert_url_contains(context, text)

