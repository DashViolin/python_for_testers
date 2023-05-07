from selenium.webdriver.common.by import By
from model.users_data import ContactForm


class ContactsHelper:
    def __init__(self, app):
        self.app = app

    def fill_form(self, contact_form: ContactForm, edition_mode=False):
        self.app.wd.find_element(By.NAME, "firstname").send_keys(contact_form.firstname)
        self.app.wd.find_element(By.NAME, "middlename").send_keys(contact_form.middlename)
        self.app.wd.find_element(By.NAME, "lastname").send_keys(contact_form.lastname)
        self.app.wd.find_element(By.NAME, "nickname").send_keys(contact_form.nickname)
        self.app.wd.find_element(By.NAME, "title").send_keys(contact_form.title)
        self.app.wd.find_element(By.NAME, "company").send_keys(contact_form.company)
        self.app.wd.find_element(By.NAME, "address").send_keys(contact_form.address)
        self.app.wd.find_element(By.NAME, "home").send_keys(contact_form.home)
        self.app.wd.find_element(By.NAME, "mobile").send_keys(contact_form.mobile)
        self.app.wd.find_element(By.NAME, "work").send_keys(contact_form.work)
        self.app.wd.find_element(By.NAME, "fax").send_keys(contact_form.fax)
        self.app.wd.find_element(By.NAME, "email").send_keys(contact_form.email)
        self.app.wd.find_element(By.NAME, "email2").send_keys(contact_form.email2)
        self.app.wd.find_element(By.NAME, "email3").send_keys(contact_form.email3)
        self.app.wd.find_element(By.NAME, "homepage").send_keys(contact_form.homepage)
        self.app.wd.find_element(By.NAME, "bday").send_keys(contact_form.bday)
        self.app.wd.find_element(By.NAME, "bmonth").send_keys(contact_form.bmonth)
        self.app.wd.find_element(By.NAME, "byear").send_keys(contact_form.byear)
        self.app.wd.find_element(By.NAME, "aday").send_keys(contact_form.aday)
        self.app.wd.find_element(By.NAME, "amonth").send_keys(contact_form.amonth)
        self.app.wd.find_element(By.NAME, "ayear").send_keys(contact_form.ayear)
        # self.app.wd.find_element(By.NAME, "new_group")
        if not edition_mode:
            self.app.wd.find_element(By.XPATH, "//option[. = 'contacts']").click()
        self.app.wd.find_element(By.NAME, "address2").send_keys(contact_form.address2)
        self.app.wd.find_element(By.NAME, "phone2").send_keys(contact_form.phone)
        self.app.wd.find_element(By.NAME, "notes").send_keys(contact_form.comment)

    def add_new_contact(self):
        self.app.wd.find_element(By.LINK_TEXT, "add new").click()

    # def open_page(self):
    #     self.app.wd.find_element(By.LINK_TEXT, "input:nth-child(7)").click()
    def del_first_contact(self):
        self.app.wd.find_element(By.ID, "1").click()
        self.app.wd.find_element(By.CSS_SELECTOR, "input[value='Delete']").click()
        assert self.app.wd.switch_to.alert.text == "Delete 1 addresses?"
        self.app.wd.switch_to.alert.accept()

    def init_contact_update(self):
        self.app.wd.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .center:nth-child(8) img").click()

    def submit_contact_update(self):
        self.app.wd.find_element(By.NAME, "update").click()
