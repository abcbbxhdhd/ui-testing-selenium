from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Formpage:
    FORMPAGE_LOCATORS = {
        'NAME_FIELD': (By.ID, 'name'),
        'INTRODUCED_FIELD': (By.ID, 'introduced'),
        'DISCONTINUED_FIELD': (By.ID, 'discontinued'),
        'COMPANY_POPDOWN': (By.ID, 'company'),
        'COMPANY_FIRST_OPTION': (By.CSS_SELECTOR, 'option[value="1"]'),
        'FORM_SUBMIT_BUTTON': (By.CSS_SELECTOR, 'input[type="submit"]'),
        'FORM_CANCEL_BUTTON': (By.PARTIAL_LINK_TEXT, 'Cancel'),
        'HELP_INLINE_LABELS': (By.CLASS_NAME, 'help-inline')
    }

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, data):
        input_name = self.driver.find_element(*self.FORMPAGE_LOCATORS['NAME_FIELD'])
        input_name.click()
        input_name.send_keys(data['computer_name'])
        input_introduced = self.driver.find_element(*self.FORMPAGE_LOCATORS['INTRODUCED_FIELD'])
        input_introduced.click()
        input_introduced.send_keys(data['introduced'])
        input_discontinued = self.driver.find_element(*self.FORMPAGE_LOCATORS['DISCONTINUED_FIELD'])
        input_discontinued.click()
        input_discontinued.send_keys(data['discontinued'])
        popdown_company = self.driver.find_element(*self.FORMPAGE_LOCATORS['COMPANY_POPDOWN'])
        popdown_company.click()
        self.driver.find_element(*self.FORMPAGE_LOCATORS['COMPANY_FIRST_OPTION']).click()
        self.driver.implicitly_wait(3)

    def submit_form(self):
        self.driver.find_element(*self.FORMPAGE_LOCATORS['FORM_SUBMIT_BUTTON']).click()

    def cancel_form(self):
        self.driver.find_element(*self.FORMPAGE_LOCATORS['FORM_CANCEL_BUTTON']).click()

    def get_help_inline_elements(self):
        return WebDriverWait(self.driver, 5)\
            .until(ec.visibility_of_any_elements_located(self.FORMPAGE_LOCATORS['HELP_INLINE_LABELS']))