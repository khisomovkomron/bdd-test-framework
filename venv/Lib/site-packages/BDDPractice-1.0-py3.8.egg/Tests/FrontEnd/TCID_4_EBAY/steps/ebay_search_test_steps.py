from BDDCommon.CommonFuncs import webcommon
from behave import given, when, then
from BDDCommon.CommonConfigs.locatorsconfig import EBAY
from BDDCommon.CommonConfigs.loggerconfigs import Logger

# logger = Logger(logLevel=logging.DEBUG)


@given('TCID-4: go to "{url}" page')
def tcid_4_go_to_page(context, url):

    webcommon.go_to(context, url)
    logger.info("GO to PAGE {}".format(url))

@given('TCID-4: search for "{item}"')
def tcid_4_search_for_item(context, item):

    search_bar = EBAY['search bar']
    search_bar_type = search_bar['type']
    search_bar_locator = search_bar['locator']
    webcommon.type_into_element(context, item, search_bar_type, search_bar_locator)
    logger.info("Typing into element: search bar")
    search_button = EBAY['search button']
    search_button_type = search_button['type']
    search_button_locator = search_button['locator']
    webcommon.click(context, search_button_type, search_button_locator)
    logger.info("Clicking element: search button")



@given("TCID-4: save the total number of result")
def tcid_4_save_results_and_verify(context):

    search_quantity = EBAY['search quantity']
    search_quantity_type = search_quantity['type']
    search_quantity_locator = search_quantity['locator']
    text1 = webcommon.get_element_text(context, search_quantity_type, search_quantity_locator)

    all_button = EBAY['all button']
    all_button_type = all_button['type']
    all_button_locator = all_button['locator']
    webcommon.click(context, all_button_type, all_button_locator)

    text2 = webcommon.get_element_text(context, search_quantity_type, search_quantity_locator)

    assert text1 < text2, "Quantity of all products is less than the quantity in category"


@when("TCID-4: navigate back to previous research result page")
def tcid_4_navigate_back(context):

    webcommon.back(context)

    #     verify that "wooden spoon" is displayed in the search box

    search_bar = EBAY['search bar']
    search_bar_type = search_bar['type']
    search_bar_locator = search_bar['locator']
    # search = webcommon.find_element(context, search_bar_type, search_bar_locator)
    search_text = webcommon.get_element_attribute(context, search_bar_type, search_bar_locator, attribute="value")
    assert search_text == "wooden spoon", "Text is not equal"


@then("TCID-4: navigate back to home page")
def tcid_4_navigate_back_to_home_page(context):

    webcommon.back(context)
    search_bar = EBAY['search bar']
    search_bar_type = search_bar['type']
    search_bar_locator = search_bar['locator']
    # search = webcommon.find_element(context, search_bar_type, search_bar_locator)
    search_text = webcommon.get_element_attribute(context, search_bar_type, search_bar_locator, attribute="value")
    assert search_text == "", "Text is not equal"




