from selenium.webdriver.common.by import By
from model.users_data import PersonalData
from model.users_data import Contacts
from model.users_data import DateFields
from model.users_data import FillComments
from model.users_data import FillContacts


class ContactsHelper:
    def __init__(self, app):
        self.app = app

    def fill_comments(self, fill_comments: FillComments):
        self.app.wd.find_element(By.NAME, "notes").send_keys(fill_comments.comment)

    def fill_contacts(self, fill_address: FillContacts):
        self.app.wd.find_element(By.XPATH, "//option[. = 'contacts']").click()
        self.app.wd.find_element(By.NAME, "address2").send_keys(fill_address.address)
        self.app.wd.find_element(By.NAME, "phone2").send_keys(fill_address.phone)

    def fill_date_fields(self, date_fields: DateFields):
        self.app.wd.find_element(By.NAME, "bday").send_keys(date_fields.bday)
        self.app.wd.find_element(By.NAME, "bmonth").send_keys(date_fields.bmonth)
        self.app.wd.find_element(By.NAME, "byear").send_keys(date_fields.byear)
        self.app.wd.find_element(By.NAME, "aday").send_keys(date_fields.aday)
        self.app.wd.find_element(By.NAME, "amonth").send_keys(date_fields.amonth)
        self.app.wd.find_element(By.NAME, "ayear").send_keys(date_fields.ayear)
        dropdown = self.app.wd.find_element(By.NAME, "new_group")
        return dropdown

    def fill_form(self, fill_contacts: Contacts):
        self.app.wd.find_element(By.NAME, "address").send_keys(fill_contacts.address)
        self.app.wd.find_element(By.NAME, "home").send_keys(fill_contacts.home)
        self.app.wd.find_element(By.NAME, "mobile").send_keys(fill_contacts.mobile)
        self.app.wd.find_element(By.NAME, "work").send_keys(fill_contacts.work)
        self.app.wd.find_element(By.NAME, "fax").send_keys(fill_contacts.fax)
        self.app.wd.find_element(By.NAME, "email").send_keys(fill_contacts.email)
        self.app.wd.find_element(By.NAME, "email2").send_keys(fill_contacts.email2)
        self.app.wd.find_element(By.NAME, "email3").send_keys(fill_contacts.email3)
        self.app.wd.find_element(By.NAME, "homepage").send_keys(fill_contacts.homepage)

    def fill_personal_data_form(self, personal_data: PersonalData):
        self.app.wd.find_element(By.NAME, "title").send_keys(personal_data.title)
        self.app.wd.find_element(By.NAME, "company").send_keys(personal_data.company)
        self.app.wd.find_element(By.NAME, "firstname").send_keys(personal_data.firstname)
        self.app.wd.find_element(By.NAME, "middlename").send_keys(personal_data.middlename)
        self.app.wd.find_element(By.NAME, "lastname").send_keys(personal_data.lastname)
        self.app.wd.find_element(By.NAME, "nickname").send_keys(personal_data.nickname)

    def add_new_contact(self):
        self.app.wd.find_element(By.LINK_TEXT, "add new").click()

    def open_page(self):
        self.app.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
