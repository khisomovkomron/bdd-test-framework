

AMAZON = {
    'search bar': {'type': 'id', 'locator': 'twotabsearchtextbox'},

}

AMAZON_HOME = {
    'button': {'type': 'xpath', 'locator': '/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input'},
    'search result': {'type': 'xpath', 'locator': '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'},


}


WIKI = {
    'search bar': {'type': 'id', 'locator': 'searchInput'},
    'button': {'type': 'css selector', 'locator': '#search-form  fieldset  button  i'},
    'search result': {'type': 'xpath', 'locator': '//*[@id="mw-content-text"]/div[3]/ul/li[1]/div[1]/a'},

}

GOOGLE = {
    'search bar': {'type': 'css selector', 'locator': '.a4bIc > input[role="combobox"]'},
    'search button': {'type': 'xpath', 'locator': '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'},
    'result link': {'type': 'xpath', 'locator': '//*[@id="rso"]/div[1]/div/div/div[1]/a/div/cite/text()'},
    'search result': {'type': 'xpath', 'locator': '//*[@id="rso"]/div[1]'},
    # ' ': {'type': 'xpath', 'locator': ''},

}

EBAY = {
    'search bar': {'type': 'id', 'locator': 'gh-ac'},
    'search button': {'type': 'id', 'locator': 'gh-btn'},
    'search quantity': {'type': 'xpath', 'locator': '//*[@id="mainContent"]/div[1]/div/div[2]/div/div[1]/h1/span[1]'},
    'all button': {'type': 'xpath', 'locator': '//*[@id="x-refine__group__0"]/ul/li/a/span'},


}

VYTRACK = {
    ' ': {'type': 'id', 'locator': ' '},
    ' ': {'type': 'css selector', 'locator': ''},
    ' ': {'type': 'xpath', 'locator': ''},

}

# Template = {
#     ' ': {'type': 'id', 'locator': ' '},
#     ' ': {'type': 'css selector', 'locator': ''},
#     ' ': {'type': 'xpath', 'locator': ''},
#
# }
