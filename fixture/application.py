from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contacts import ContactsHelper
from fixture.groups import GroupsHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.session = SessionHelper(self)
        self.contacts = ContactsHelper(self)
        self.groups = GroupsHelper(self)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()


