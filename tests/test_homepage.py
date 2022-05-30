from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.page_object.pages.home_page import Homepage


def test_nav_to_home_page(driver):
    homepage = Homepage(driver)
    homepage.nav_to_add_computer()
    driver.find_element(By.CSS_SELECTOR, 'a.fill').click()
    assert homepage.get_label_amount_of_computers_text() == '574 computers found'

def test_add_new_computer(driver):
    homepage = Homepage(driver)
    new_computer_data = {
        'computer_name': 'New Computer',
        'introduced': '2022-05-29',
        'discontinued': '2022-05-30'
    }
    homepage.nav_to_add_computer()
    input_name = driver.find_element(By.ID, 'name')
    input_name.click()
    input_name.send_keys(new_computer_data['computer_name'])
    input_introduced = driver.find_element(By.ID, 'introduced')
    input_introduced.click()
    input_introduced.send_keys(new_computer_data['introduced'])
    input_discontinued = driver.find_element(By.ID, 'discontinued')
    input_discontinued.click()
    input_discontinued.send_keys(new_computer_data['discontinued'])
    popdown_company = driver.find_element(By.ID, 'company')
    popdown_company.click()
    driver.find_element(By.CSS_SELECTOR, 'option[value="1"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    driver.implicitly_wait(3)
    assert homepage.get_new_computer_alert_text() == 'Done !'

def test_filter_computers_by_name(driver):
    homepage = Homepage(driver)
    input = 'ARRA'
    homepage.filter_computers_by_name(input)
    found_name = driver.find_element(By.PARTIAL_LINK_TEXT, input).text
    assert found_name == input

def test_search_unexisting_computer(driver):
    homepage = Homepage(driver)
    input = 'My Computer'
    homepage.filter_computers_by_name(input)
    assert homepage.get_unexisting_computer_label_text() == 'Nothing to display'

def test_cancel_the_form(driver):
    homepage = Homepage(driver)
    driver.find_element(By.ID, 'add').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Cancel').click()
    driver.implicitly_wait(3)
    assert homepage.get_label_amount_of_computers_text() == '574 computers found'

def test_fill_the_form_empty_company_name(driver):
    driver.find_element(By.ID, 'add').click()
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    label_name_required = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, 'help-inline')))
    assert label_name_required.text == 'Failed to refine type : Predicate isEmpty() did not fail.'

def test_fill_the_form_incorrect_date_format_introduced(driver):
    driver.find_element(By.ID, 'add').click()
    new_computer_data = {
        'computer_name': 'My Computer',
        'introduced': '05-05-2020',
        'discontinued': '05-05-2020'
    }
    input_name = driver.find_element(By.ID, 'name')
    input_name.click()
    input_name.send_keys(new_computer_data['computer_name'])
    input_introduced = driver.find_element(By.ID, 'introduced')
    input_introduced.click()
    input_introduced.send_keys(new_computer_data['introduced'])
    input_discontinued = driver.find_element(By.ID, 'discontinued')
    input_discontinued.click()
    input_discontinued.send_keys(new_computer_data['discontinued'])
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    labels_wrong_date_format = WebDriverWait(driver, 5).until(ec.visibility_of_any_elements_located((By.CLASS_NAME, 'help-inline')))
    for label in labels_wrong_date_format[1:]:
        assert label.text == "Failed to decode date : java.time.format.DateTimeParseException: Text '" + new_computer_data['introduced'] +  "' could not be parsed at index 0"

def test_computer_list_pagination(driver):
    homepage = Homepage(driver)
    homepage.nav_to_next_pagination()
    homepage.nav_to_prev_pagination()
    assert homepage.get_prev_button_class() == 'prev disabled'
