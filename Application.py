from selenium import webdriver
from selenium.webdriver.common.by import By
from users_data import PersonalData
from users_data import OptionalFields
from users_data import Contacts
from users_data import DateFields
from users_data import FillComments
from users_data import FillContacts


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def open_home_page_before_logout(self):
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.wd.find_element(By.LINK_TEXT, "home").click()

    def fill_comments(self, fill_comments: FillComments):
        self.wd.find_element(By.NAME, "notes").send_keys(fill_comments.comment)

    def fill_contacts(self, fill_address: FillContacts):
        self.wd.find_element(By.XPATH, "//option[. = 'contacts']").click()
        self.wd.find_element(By.NAME, "address2").send_keys(fill_address.address)
        self.wd.find_element(By.NAME, "phone2").send_keys(fill_address.phone)

    def fill_date_fields(self, date_fields: DateFields):
        self.wd.find_element(By.NAME, "bday").send_keys(date_fields.bday)
        self.wd.find_element(By.NAME, "bmonth").send_keys(date_fields.bmonth)
        self.wd.find_element(By.NAME, "byear").send_keys(date_fields.byear)
        self.wd.find_element(By.NAME, "aday").send_keys(date_fields.aday)
        self.wd.find_element(By.NAME, "amonth").send_keys(date_fields.amonth)
        self.wd.find_element(By.NAME, "ayear").send_keys(date_fields.ayear)
        dropdown = self.wd.find_element(By.NAME, "new_group")
        return dropdown

    def fill_contact_form(self, fill_contacts: Contacts):
        self.wd.find_element(By.NAME, "address").send_keys(fill_contacts.address)
        self.wd.find_element(By.NAME, "home").send_keys(fill_contacts.home)
        self.wd.find_element(By.NAME, "mobile").send_keys(fill_contacts.mobile)
        self.wd.find_element(By.NAME, "work").send_keys(fill_contacts.work)
        self.wd.find_element(By.NAME, "fax").send_keys(fill_contacts.fax)
        self.wd.find_element(By.NAME, "email").send_keys(fill_contacts.email)
        self.wd.find_element(By.NAME, "email2").send_keys(fill_contacts.email2)
        self.wd.find_element(By.NAME, "email3").send_keys(fill_contacts.email3)
        self.wd.find_element(By.NAME, "homepage").send_keys(fill_contacts.homepage)

    def fill_optional_fields(self, optional_fields: OptionalFields):
        self.wd.find_element(By.NAME, "title").send_keys(optional_fields.title)
        self.wd.find_element(By.NAME, "company").send_keys(optional_fields.company)

    def add_picture(self):
        self.wd.find_element(By.NAME, "photo").send_keys(
            r"C:\Users\user\Pictures\Фоновые изображения рабочего стола\4. Кот с наушниками.jpg")

    def fill_personal_data_form(self, personal_data: PersonalData):
        self.wd.find_element(By.NAME, "firstname").send_keys(personal_data.firstname)
        self.wd.find_element(By.NAME, "middlename").send_keys(personal_data.middlename)
        self.wd.find_element(By.NAME, "lastname").send_keys(personal_data.lastname)
        self.wd.find_element(By.NAME, "nickname").send_keys(personal_data.nickname)

    def add_new_contact(self):
        self.wd.find_element(By.LINK_TEXT, "add new").click()

    def open_contact_page(self):
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def login(self, username, password):
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").send_keys(password)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
