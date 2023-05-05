from fixture.application import Application


def test_del_first_group(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.groups.open_groups_page()
    app.groups.del_first_group()
    app.open_home_page()
    app.session.logout()
