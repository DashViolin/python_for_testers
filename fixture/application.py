from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper
from fixture.contacts import ContactsHelper
from fixture.groups import GroupsHelper


class Application:
    def __init__(self):
        self.wait = 3
        self.wd = webdriver.Firefox()
        self.session = SessionHelper(self)
        self.contacts = ContactsHelper(self)
        self.groups = GroupsHelper(self)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")
        if self.session.is_logon:
            WebDriverWait(self.wd, self.wait).until(ec.visibility_of_element_located((By.ID, "footer")))
        else:
            WebDriverWait(self.wd, self.wait).until(ec.visibility_of_element_located((By.LINK_TEXT, "Create account")))

    def destroy(self):
        self.wd.quit()
