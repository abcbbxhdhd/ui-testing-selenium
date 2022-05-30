from selenium.webdriver.common.by import By

from src.page_object.pages.home_page import Homepage
from src.page_object.pages.form_page import Formpage


def test_nav_to_home_page(driver):
    homepage = Homepage(driver)

    homepage.nav_to_add_computer()
    driver.find_element(By.CSS_SELECTOR, 'a.fill').click()
    assert homepage.get_label_amount_of_computers_text() == '574 computers found'

def test_add_new_computer(driver):
    homepage = Homepage(driver)
    formpage = Formpage(driver)

    new_computer_data = {
        'computer_name': 'New Computer',
        'introduced': '2022-05-29',
        'discontinued': '2022-05-30'
    }
    homepage.nav_to_add_computer()
    formpage.fill_form(new_computer_data)
    formpage.submit_form()
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
    formpage = Formpage(driver)

    homepage.nav_to_add_computer()
    formpage.cancel_form()
    driver.implicitly_wait(3)
    assert homepage.get_label_amount_of_computers_text() == '574 computers found'

def test_fill_the_form_empty_company_name(driver):
    homepage = Homepage(driver)
    formpage = Formpage(driver)

    homepage.nav_to_add_computer()
    formpage.submit_form()
    assert formpage.get_help_inline_elements()[0].text == 'Failed to refine type : Predicate isEmpty() did not fail.'

def test_fill_the_form_incorrect_date_format_introduced(driver):
    homepage = Homepage(driver)
    formpage = Formpage(driver)

    new_computer_data = {
        'computer_name': 'My Computer',
        'introduced': '05-05-2020',
        'discontinued': '05-05-2020'
    }
    homepage.nav_to_add_computer()
    formpage.fill_form(new_computer_data)
    formpage.submit_form()
    for label in formpage.get_help_inline_elements()[1:]:
        assert label.text == "Failed to decode date : java.time.format.DateTimeParseException: Text '" + new_computer_data['introduced'] +  "' could not be parsed at index 0"

def test_computer_list_pagination(driver):
    homepage = Homepage(driver)
    homepage.nav_to_next_pagination()
    homepage.nav_to_prev_pagination()
    assert homepage.get_prev_button_class() == 'prev disabled'
