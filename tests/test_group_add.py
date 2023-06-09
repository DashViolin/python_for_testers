from fixture.application import Application
from model.group import Group


def test_group_add(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.groups.open_groups_page()
    app.groups.init_group_creation()
    group = Group(name="123", header="456", footer="abc")
    app.groups.fill_group_form(group)
    app.groups.submit_group_creation()
    app.groups.open_groups_page()
    app.session.logout()


def test_empty_group_add(app: Application):
    group = Group(name="", header="", footer="")
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.groups.open_groups_page()
    app.groups.init_group_creation()
    app.groups.fill_group_form(group)
    app.groups.submit_group_creation()
    app.groups.open_groups_page()
    app.session.logout()
