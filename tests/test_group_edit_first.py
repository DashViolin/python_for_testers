from fixture.application import Application
from model.group import Group


def test_group_edit_first(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.groups.open_groups_page()
    app.groups.init_group_edition()
    group = Group(name="xyz", header="", footer="")
    app.groups.fill_group_form(group)
    app.groups.submit_group_update()
    app.groups.open_groups_page()
    app.session.logout()
