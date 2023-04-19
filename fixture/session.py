from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.wd.find_element(By.NAME, "user").send_keys(username)
        self.app.wd.find_element(By.NAME, "pass").send_keys(password)
        self.app.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER)
        WebDriverWait(self.app.wd, 5).until(ec.visibility_of_element_located((By.ID, "footer")))

    def logout(self):
        self.app.open_home_page()
        self.app.wd.find_element(By.LINK_TEXT, "Logout").click()
