from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contacts import ContactsHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.mgr = HelperManager(self)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()


class HelperManager:
    def __init__(self, app):
        self.session = SessionHelper(app)
        self.contacts = ContactsHelper(app)
