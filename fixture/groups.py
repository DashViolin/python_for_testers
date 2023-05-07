from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class GroupsHelper:
    def __init__(self, app):
        self.app = app

    def submit_group_creation(self):
        self.app.wd.find_element(By.NAME, "submit").click()
        WebDriverWait(self.app.wd, self.app.wait).until(ec.visibility_of_element_located((By.ID, "footer")))

    def fill_group_form(self, group):
        self.app.wd.find_element(By.NAME, "group_name").click()
        self.app.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.wd.find_element(By.NAME, "group_header").click()
        self.app.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.wd.find_element(By.NAME, "group_footer").click()
        self.app.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def init_group_creation(self):
        self.app.wd.find_element(By.NAME, "new").click()
        WebDriverWait(self.app.wd, self.app.wait).until(ec.visibility_of_element_located((By.ID, "footer")))

    def open_groups_page(self):
        self.app.wd.find_element(By.LINK_TEXT, "groups").click()
        WebDriverWait(self.app.wd, self.app.wait).until(ec.visibility_of_element_located((By.ID, "footer")))

    def del_first_group(self):
        self.app.wd.find_element(By.NAME, "selected[]").click()
        self.app.wd.find_element(By.NAME, "delete").click()

    def init_group_edition(self):
        self.app.wd.find_element(By.CSS_SELECTOR, "input[value='1']").click()
        self.app.wd.find_element(By.NAME, "edit").click()
        WebDriverWait(self.app.wd, self.app.wait).until(ec.visibility_of_element_located((By.ID, "footer")))

    def submit_group_update(self):
        self.app.wd.find_element(By.NAME, "update").click()
        WebDriverWait(self.app.wd, self.app.wait).until(ec.visibility_of_element_located((By.ID, "footer")))
