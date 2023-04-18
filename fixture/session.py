from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.wd.find_element(By.NAME, "user").send_keys(username)
        self.app.wd.find_element(By.NAME, "pass").send_keys(password)

    def logout(self):
        self.app.wd.find_element(By.LINK_TEXT, "Logout").click()
