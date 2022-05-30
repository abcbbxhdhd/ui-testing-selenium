from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def nav_to_add_computer(self):
        self.driver.find_element(By.ID, 'add').click()

    def get_new_computer_alert_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.alert-message strong').text

    def filter_computers_by_name(self, computer_name):
        input_search = self.driver.find_element(By.ID, 'searchbox')
        input_search.click()
        input_search.send_keys(computer_name)
        self.driver.find_element(By.ID, 'searchsubmit').click()
        self.driver.implicitly_wait(3)

    def get_unexisting_computer_label_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.well em').text

    def nav_to_next_pagination(self):
        button_nav_next = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Next →')
        button_nav_next.click()
        self.driver.implicitly_wait(3)

    def nav_to_prev_pagination(self):
        button_nav_prev = self.driver.find_element(By.PARTIAL_LINK_TEXT, '← Previous')
        button_nav_prev.click()
        self.driver.implicitly_wait(3)

    def get_prev_button_class(self):
        return self.driver.find_element(By.ID, 'pagination').find_elements(By.TAG_NAME, 'li')[0].get_attribute('class')

    def get_label_amount_of_computers_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'section[id="main"] h1').text