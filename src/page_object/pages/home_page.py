from selenium.webdriver.common.by import By


class Homepage:
    HOMEPAGE_LOCATORS = {
        'ADD_BUTTON': (By.ID, 'add'),
        'NEW_COMPUTER_ALERT': (By.CSS_SELECTOR, 'div.alert-message strong'),
        'SEARCH_INPUT': (By.ID, 'searchbox'),
        'SUBMIT_SEARCH_BUTTON': (By.ID, 'searchsubmit'),
        'UNEXISTING_COMPUTER_LABEL': (By.CSS_SELECTOR, 'div.well em'),
        'NEXT_PAGE_BUTTON': (By.PARTIAL_LINK_TEXT, 'Next →'),
        'PREV_PAGE_BUTTON': (By.PARTIAL_LINK_TEXT, '← Previous'),
        'PAGINATION_CONTAINER': (By.ID, 'pagination'),
        'LI_TAG': (By.TAG_NAME, 'li'),
        'COMPUTER_AMOUNT_MAIN_LABEL': (By.CSS_SELECTOR, 'section[id="main"] h1')
    }

    def __init__(self, driver):
        self.driver = driver

    def nav_to_add_computer(self):
        self.driver.find_element(*self.HOMEPAGE_LOCATORS['ADD_BUTTON']).click()

    def get_new_computer_alert_text(self):
        return self.driver.find_element(*self.HOMEPAGE_LOCATORS['NEW_COMPUTER_ALERT']).text

    def filter_computers_by_name(self, computer_name):
        input_search = self.driver.find_element(*self.HOMEPAGE_LOCATORS['SEARCH_INPUT'])
        input_search.click()
        input_search.send_keys(computer_name)
        self.driver.find_element(*self.HOMEPAGE_LOCATORS['SUBMIT_SEARCH_BUTTON']).click()
        self.driver.implicitly_wait(3)

    def get_unexisting_computer_label_text(self):
        return self.driver.find_element(*self.HOMEPAGE_LOCATORS['UNEXISTING_COMPUTER_LABEL']).text

    def nav_to_next_pagination(self):
        button_nav_next = self.driver.find_element(*self.HOMEPAGE_LOCATORS['NEXT_PAGE_BUTTON'])
        button_nav_next.click()
        self.driver.implicitly_wait(3)

    def nav_to_prev_pagination(self):
        button_nav_prev = self.driver.find_element(*self.HOMEPAGE_LOCATORS['PREV_PAGE_BUTTON'])
        button_nav_prev.click()
        self.driver.implicitly_wait(3)

    def get_prev_button_class(self):
        return self.driver\
            .find_element(*self.HOMEPAGE_LOCATORS['PAGINATION_CONTAINER'])\
            .find_elements(*self.HOMEPAGE_LOCATORS['LI_TAG'])[0]\
            .get_attribute('class')

    def get_label_amount_of_computers_text(self):
        return self.driver.find_element(*self.HOMEPAGE_LOCATORS['COMPUTER_AMOUNT_MAIN_LABEL']).text