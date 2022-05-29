import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_nav_to_home_page(driver):
    driver.find_element(By.ID, 'add').click()
    driver.find_element(By.CSS_SELECTOR, 'a.fill').click()
    home_page_label = driver.find_element(By.CSS_SELECTOR, 'section[id="main"] h1').text
    assert home_page_label == '574 computers found'

def test_add_new_computer(driver):
    new_computer_data = {
        'computer_name': 'New Computer',
        'introduced': '2022-05-29',
        'discontinued': '2022-05-30'
    }
    driver.find_element(By.ID, 'add').click()
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
    alert_new_computer = driver.find_element(By.CSS_SELECTOR, 'div.alert-message strong')
    assert alert_new_computer.text == 'Done !'

def test_filter_computers_by_name(driver):
    input = 'ARRA'
    input_search = driver.find_element(By.ID, 'searchbox')
    input_search.click()
    input_search.send_keys(input)
    driver.find_element(By.ID, 'searchsubmit').click()
    driver.implicitly_wait(3)
    found_name = driver.find_element(By.PARTIAL_LINK_TEXT, input).text
    assert found_name == input

def test_search_unexisting_computer(driver):
    input = 'My Computer'
    input_search = driver.find_element(By.ID, 'searchbox')
    input_search.click()
    input_search.send_keys(input)
    driver.find_element(By.ID, 'searchsubmit').click()
    driver.implicitly_wait(3)
    label_nothing_to_display = driver.find_element(By.CSS_SELECTOR, 'div.well em').text
    assert label_nothing_to_display == 'Nothing to display'

def test_cancel_the_form(driver):
    driver.find_element(By.ID, 'add').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Cancel').click()
    driver.implicitly_wait(3)
    home_page_label = driver.find_element(By.CSS_SELECTOR, 'section[id="main"] h1').text
    assert home_page_label == '574 computers found'

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
    first_page_first_element = 'ACE'
    second_page_first_element = 'ASCI White'
    button_nav_next = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next →')
    button_nav_next.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, second_page_first_element)))
    button_nav_prev = driver.find_element(By.PARTIAL_LINK_TEXT, '← Previous')
    button_nav_prev.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, first_page_first_element)))
    li_previous = driver.find_element(By.ID, 'pagination').find_elements(By.TAG_NAME, 'li')[0]
    assert li_previous.get_attribute('class') == 'prev disabled'
