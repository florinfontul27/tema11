from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL_INPUT_NEW_ACCOUNT = (By.ID, "email_create")
    CLICK_RADIO_BUTTON = (By.ID, "uniform-id_gender1")
    FIRST_NAME_INPUT = (By.ID, "customer_firstname")
    LAST_NAME_INPUT = (By.ID, "customer_lastname")
    CHECK_FIRST_BOX = (By.ID, "agree_terms")
    CHECK_SECOND_BOX = (By.ID, "agree_newsletter")
    CHECK_THIRD_BOX = (By.ID, "agree_age")
    CLICK_SUBMIT_BUTTON = (By.ID, "submitAccount")
    SUCCES_MESSAGE = (By.CLASS_NAME, "alert alert-success")
    CHECK_NAME_IS_DISPLAYED = (By.CLASS_NAME, "icon icon-cafeo-oameni hidden-xs")

    def __init__(self, browser):
        self.browser = browser

    def type_email_new_account(self,email_new_account):
        self.browser.find_element(*self.EMAIL_INPUT_NEW_ACCOUNT).send_keys(email_new_account)

    def click_radio_button(self):
        self.browser.find_element(*self.CLICK_RADIO_BUTTON).click()

    def type_first_name(self, first_name):
        self.browser.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def type_last_name(self, last_name):
        self.browser.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def check_the_first_box(self):
        self.browser.find_element(*self.CHECK_FIRST_BOX).click()

    def check_the_second_box(self):
        self.browser.find_element(*self.CHECK_SECOND_BOX)

    def check_the_third_box(self):
        self.browser.find_element(*self.CHECK_THIRD_BOX)

    def click_submit_button(self):
        self.browser.find_element(*self.CLICK_SUBMIT_BUTTON)

    def get_succes_messge(self):
        return self.browser.find_element(*self.SUCCES_MESSAGE).text

    def check_if_name_is_displayed(self):
        return self.browser.find_element(*self.CHECK_NAME_IS_DISPLAYED).text
