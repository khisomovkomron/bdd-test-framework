from behave import step, given, when, then
from BDDCommon.CommonConfigs.locatorsconfig import GOOGLE
from BDDCommon.CommonFuncs import webcommon
from selenium import webdriver
import time

@given("TCID-3: user goes to '{url}' page")
def tcid_3_go_to_page(context, url):

    webcommon.go_to(context, url)


@given('TCID-3: search for one of the strings the list item given below')
def tcid_3_search_for_items_from_list(context):

    search_list = ["cucumber", "java", "selenium web browser automation"]
    for i in search_list:
        search_bar = GOOGLE['search bar']
        search_bar_type = search_bar['type']
        search_bar_locator = search_bar['locator']
        webcommon.type_into_element(context, i, search_bar_type, search_bar_locator)
        search_button = GOOGLE['search button']
        search_button_type = search_button['type']
        search_button_locator = search_button['locator']
        webcommon.click(context, search_button_type, search_button_locator)
        webcommon.back(context)


@given("TCID-3: in the results pages, capture the url right above the first result")
def tcid_3_capture_link(context):

    result_link = GOOGLE['result link']
    result_link_type = result_link['type']
    result_link_locator = result_link['locator']
    text = webcommon.get_element_text(context, result_link_type, result_link_locator)

    search_result = GOOGLE['search result']
    search_result_type = search_result['type']
    search_result_locator = search_result['locator']
    webcommon.click(context, search_result_type, search_result_locator)

    webcommon.assert_url_contains(context, text)


